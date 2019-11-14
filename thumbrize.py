#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from PIL import Image

SUFFIX = '_thumbnail'

def create_thumbnail(input, size, output='.'):
    MAX_SIZE = (size, size)
    images_files = find_files(input) # routines to find all files in the directory.
    for infile in images_files:
        extension = ''
        file, extension = os.path.splitext(infile)
        # condition to convert the jpg (MS-DOS 8.3 and FAT-16 file system)
        # file formt to JPEG.
        if extension == '.jpg':
            extension = 'JPEG'
        im = Image.open(infile)
        im.thumbnail(MAX_SIZE)
        if extension == '.png':
            # to save the png images as thumbnails.
            im.save(file + SUFFIX, 'png', quality=80)
        else:
            # to save the JPEG images as thumbnails.
            im.save(file + SUFFIX, extension.upper(), quality=80)

# routines find the specified images format file from the mentioned
# directory packed into a list
def find_files(input):
    filenames = []
    for root, _, files in os.walk(input):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                filenames.append(os.path.join(root, file))
    return filenames

def main(argv=None):

    parser = argparse.ArgumentParser(description='Tool for image resize')
    parser.add_argument(
        '-i',
        metavar='input file',
        required=True,
        help='input files for converting a thumbnail.')
    parser.add_argument(
        '-o',
        metavar='out file',
        required=True,
        help='out file or directory to save the thumbnails')
    parser.add_argument(
        '-s',
        metavar='size',
        type=int,
        required=True,
        help='size of the thumbnails')
    args = parser.parse_args(argv)
    create_thumbnail(args.i, args.s, args.o)

if __name__ == '__main__':  
    main()
