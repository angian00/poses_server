#!/usr/bin/env python

import os
import os.path
import logging
import random


def build_file_list():
    root_image_dir = "data/poses"
    file_list = []

    for root, subdirs, files in os.walk(root_image_dir):
        for filename in files:
            full_file_path = os.path.join(root, filename)
            logging.info("Indexing file: " + full_file_path)
            file_list.append(full_file_path)

    return file_list


if __name__ == "__main__":
    filenames = build_file_list()
    
    ## DEBUG
    #print "Content-type: text/plain\n"
    #for f in filenames:
    #    print f
    #

    filename = "/" + random.choice(filenames)
    #filename = "/data/poses/Sekaa_Small/Sekaa_Small567.jpg"

    #print "Content-type: image/jpeg\n"
    #print file(filename, "rb").read()

    print "Content-type: text/html\n"
    print '<html>'
    print '<head>'
    print '<title>Random pose generator</title>'
    print '</head>'

    print '<body>'
    print '<img src="%s">' % filename
    print '</body>'
    print '</html>'

