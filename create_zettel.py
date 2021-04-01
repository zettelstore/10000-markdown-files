#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
create_zettel: create a directory file files to be readable by Zettelstore.
"""

import pathlib
import shutil

ZETTEL_DIR = "zettel"

def create_zettel_dir():
    """Create a new, empty 'zettel' directory."""
    try:
        shutil.rmtree(ZETTEL_DIR)
    except OSError as exc:
        print(exc)
    result = pathlib.Path(ZETTEL_DIR)
    result.mkdir()
    return result

def copy_zettel(frompath, topath):
    """Copy the file at frompath to topath."""
    shutil.copyfile(frompath, topath)

def make_meta(metapath, title):
    """Create metafile."""
    with open(metapath, "wt") as mfile:
        print("title:", title.capitalize(), file=mfile)

def main():
    """Main function."""
    zetteldir = create_zettel_dir()
    filesdir = pathlib.Path("files.md")
    zid = 10000000000000
    for _ in range(2):
        for fpath in filesdir.iterdir():
            if not fpath.is_file():
                continue
            copy_zettel(fpath, zetteldir.joinpath(str(zid) + " " + fpath.name))
            make_meta(zetteldir.joinpath(str(zid) + " " + fpath.stem + ".meta"), fpath.stem)
            zid += 100

if __name__ == '__main__':
    main()
