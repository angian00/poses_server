#!/usr/bin/env python

import os
import os.path

index_file_path = "index.txt"


def build_file_list():
    root_image_dir = "data/poses"
    file_list = []

    for root, subdirs, files in os.walk(root_image_dir):
        for filename in files:
            full_file_path = os.path.join(root, filename)
            file_list.append(full_file_path)

    return file_list


if __name__ == "__main__":
    filenames = build_file_list()
    

    with open(index_file_path, 'w') as index_file:
        for fn in filenames:
            print >>index_file, fn
