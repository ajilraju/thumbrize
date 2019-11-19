#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from PIL import Image

SUFFIX = '_thumbnail'

def create_thumbnail(infile, size, output, recur=False):

    MAX_SIZE = (size, size)
    images_files = find_files(infile) # routines to find all files in the directory.
    for infile in images_files:
        extension = ''
        file, extension = os.path.splitext(infile)
        if output != None: file = output
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
def find_files(insource):
    filenames = []
    for root, _, files in os.walk(insource):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                filenames.append(os.path.join(root, file))
    return filenames

def main():

    pwd = os.getcwd()
    
    parser = argparse.ArgumentParser(description='Tool for image resize')
    parser.add_argument('infile',
                        help='File for the resize')
    parser.add_argument('size',
                        type=int,
                        help='Image resizing scale factor')
    parser.add_argument('-o',
                        '--outfile',
                        default=pwd,
                        help='To store the resized images')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='Iterate over the entire directory')
                        
    args = parser.parse_args()
    create_thumbnail(args.infile, args.size, \
                        args.outfile, args.recursive)

if __name__ == '__main__':  
    main()
