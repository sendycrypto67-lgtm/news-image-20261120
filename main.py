#!/usr/bin/env python3
"""Copy the news-image-20261120 front page to the output directory.

The entry is a single finished image, entry.png, stored beside this
file. This program checks that the image is a whole PNG within the
competition limits, copies it to the output directory, and then
checks the copy again from its own bytes, so the delivered file is
proven to be the same gate-passing image. It uses only the Python
standard library, makes no network calls, uses no randomness, and
reads no input besides the image file.
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

MAX_DIMENSION = 1024
MAX_BYTES = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
HEADER_LENGTH = 33


def read_png_size(path):
    """Return the (width, height) stored in a PNG file header.

    Raises ValueError, naming the file, when the bytes are not a PNG
    or the header is too short to hold an IHDR chunk.
    """
    with open(path, "rb") as handle:
        header = handle.read(HEADER_LENGTH)
    if len(header) < HEADER_LENGTH:
        raise ValueError("%s is too short to be a PNG file" % path)
    if header[:8] != PNG_MAGIC:
        raise ValueError("%s does not start with PNG magic bytes" % path)
    chunk_type = header[12:16]
    if chunk_type != b"IHDR":
        raise ValueError("%s has no IHDR chunk after the PNG magic" % path)
    chunk_length = struct.unpack(">I", header[8:12])[0]
    if chunk_length != 13:
        raise ValueError(
            "%s has an IHDR chunk of %d bytes, expected 13"
            % (path, chunk_length)
        )
    width, height = struct.unpack(">II", header[16:24])
    if width == 0 or height == 0:
        raise ValueError(
            "%s declares zero dimensions (%dx%d)" % (path, width, height)
        )
    return width, height


def check_png(path):
    """Check one file against the competition gates.

    Returns (width, height, size in bytes, sha256 hex digest).
    Raises ValueError, naming the file, on any failed gate.
    """
    if not path.is_file():
        raise ValueError("%s does not exist or is not a file" % path)
    size = path.stat().st_size
    if size > MAX_BYTES:
        raise ValueError(
            "%s is %d bytes, over the %d byte limit" % (path, size, MAX_BYTES)
        )
    width, height = read_png_size(path)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(
            "%s is %dx%d, over the %d pixel limit"
            % (path, width, height, MAX_DIMENSION)
        )
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return width, height, size, digest


def main():
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output = output_dir / "entry.png"

    width, height, size, digest = check_png(source)

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output)

    out_width, out_height, out_size, out_digest = check_png(output)
    assert out_size == size, "output size does not match the source"
    assert out_digest == digest, "output sha256 does not match the source"
    assert (out_width, out_height) == (width, height), (
        "output dimensions %dx%d do not match the source %dx%d"
        % (out_width, out_height, width, height)
    )
    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (output, width, height, size, digest))


if __name__ == "__main__":
    main()
