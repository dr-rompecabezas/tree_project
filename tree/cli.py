"""This module provides the command line interface (CLI) for Tree."""

import argparse
import pathlib
import sys

from . import __version__
from .tree import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(
        root_dir, 
        dir_only=args.dir_only, 
        output_file=args.output_file, 
        ignore=args.ignore
    )
    tree.generate()


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="Tree, a directory tree generator",
        epilog="Thanks for using Tree!",
    )
    parser.version = f"Tree v{__version__}"
    parser.add_argument(
        "-v",
        "--version",
        action="version",
    )
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a directory-only tree",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="Generate a full directory tree and save it to a file",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        metavar="IGNORE",
        nargs="*",
        default=[],
        help="A list of files or directories to ignore",
    )
    return parser.parse_args()
