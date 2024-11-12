import os
import sys

import cv2
import imutils
import numpy as np
from imutils import perspective
from rembg.bg import remove as rembg

APPROX_POLY_DP_ACCURACY_RATIO = 0.02
IMG_RESIZE_H = 500.0


def scan(data):
    try:
        # Read data as a byte array and remove background
        processed_data = rembg(data)
        img_array = np.frombuffer(processed_data, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)

        # Check if img was successfully decoded
        if img is None:
            raise ValueError(
                "Image decoding failed. Ensure the input data is a valid image format."
            )

        # Resize and work with a copy of the original image
        orig = img.copy()
        ratio = img.shape[0] / IMG_RESIZE_H
        img = imutils.resize(img, height=int(IMG_RESIZE_H))

        # Handle alpha channel, if present
        if img.shape[2] == 4:
            _, img = cv2.threshold(img[:, :, 3], 0, 255, cv2.THRESH_BINARY)
        else:
            raise ValueError("The image lacks an alpha channel for background removal.")

        img = cv2.medianBlur(img, 15)

        # Find contours and sort by area
        cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

        outline = None

        # Find a 4-sided polygon contour
        for c in cnts:
            perimeter = cv2.arcLength(c, True)
            polygon = cv2.approxPolyDP(
                c, APPROX_POLY_DP_ACCURACY_RATIO * perimeter, True
            )

            if len(polygon) == 4:
                outline = polygon.reshape(4, 2)
                break

        # If no outline was found, return the original image
        if outline is None:
            result = orig
        else:
            # Apply perspective transform based on the outline
            result = perspective.four_point_transform(orig, outline * ratio)

        # Encode the result to PNG format
        _, buf = cv2.imencode(".png", result)
        return buf.tobytes()

    except Exception as e:
        print(f"Error in processing: {e}", file=sys.stderr)
        return None
