import argparse
import glob
import imghdr
import os

from ..doc import scan


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "-p", "--path", nargs="+", help="Path of a file or a folder of files.",
    )

    ap.add_argument(
        "-o",
        "--output",
        nargs="?",
        default="-",
        type=argparse.FileType("wb"),
        help="Path to the output png image.",
    )

    ap.add_argument(
        "input",
        nargs="?",
        default="-",
        type=argparse.FileType("rb"),
        help="Path to the input image.",
    )

    args = ap.parse_args()

    r = lambda i: i.buffer.read() if hasattr(i, "buffer") else i.read()
    w = lambda o, data: o.buffer.write(data) if hasattr(o, "buffer") else o.write(data)

    if args.path:
        full_paths = [os.path.abspath(path) for path in args.path]
        files = set()

        for path in full_paths:
            if os.path.isfile(path):
                files.add(path)
            else:
                full_paths += glob.glob(path + "/*")

        for fi in files:
            if imghdr.what(fi) is None:
                continue

            with open(fi, "rb") as input:
                with open(os.path.splitext(fi)[0] + ".out.png", "wb") as output:
                    w(output, scan(r(input)))

    else:
        w(args.output, scan(r(args.input)))


if __name__ == "__main__":
    main()
