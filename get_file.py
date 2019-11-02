#!/usr/bin/env python3

import os
from random import randrange

def rdm(folder_path):
    """Return a random file name in the given folder"""
    path = os.path.abspath(folder_path)
    files = os.listdir(path)
    file_name = files[randrange(len(files))]
    return file_name


if __name__ in "__main__":
    print(rdm(input("Folder: ")))
