import glob
import imghdr
import os
import sys

import click
import rembg

from ..doc import scan


@click.command()
@click.argument(
    "input", default=(None if sys.stdin.isatty() else "-"), type=click.File("rb")
)
@click.argument(
    "output",
    default=(None if sys.stdin.isatty() else "-"),
    type=click.File("wb", lazy=True),
)
def main(input, output):
    output.write(rembg.remove(input.read()))


if __name__ == "__main__":
    main()
