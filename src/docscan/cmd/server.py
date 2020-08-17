import argparse
from io import BytesIO
from urllib.parse import unquote_plus
from urllib.request import urlopen

from flask import Flask, request, send_file
from waitress import serve

from ..doc import scan

app = Flask(__name__)


def index():
    url = request.args.get("url", type=str)
    if url is None:
        return {"error": "missing query param 'url'"}, 400

    try:
        return send_file(
            BytesIO(scan(urlopen(unquote_plus(url)).read())), mimetype="image/png",
        )
    except Exception as e:
        app.logger.exception(e, exc_info=True)
        return {"error": "oops, something went wrong!"}, 500


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "-a", "--addr", default="0.0.0.0", type=str, help="The IP address to bind to.",
    )

    ap.add_argument(
        "-p", "--port", default=5000, type=int, help="The port to bind to.",
    )

    args = ap.parse_args()
    app.add_url_rule("/", "index", index)
    serve(app, host=args.addr, port=args.port)


if __name__ == "__main__":
    main()
