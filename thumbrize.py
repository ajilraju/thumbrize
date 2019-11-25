#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
from PIL import Image

SUFFIX = '_thumbnail'

def create_thumbnail(infile, size, output, recur=False):

    MAX_SIZE = (size, size)
    imgfile = FileFinder(infile).find_files()
    for infile in imgfile:
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

class FileFinder(object):
    """Find the files the in the mentioned directory and also return the
    details about the implicit pointed files in the filesystem."""
    def __init__(self, infile):
        self.infile = infile
        
    def find_files(self):
        """Return the files absolute path from the input"""
        filenames = []
        content = os.path.abspath(self.infile)
        if not os.path.exists(content):
            print(content)
            print("File Not found")
            sys.exit(1)
        else:
            print(content)
            if os.path.isfile(content):
                return content
                
            else:
                for root, _, files in os.walk(insource):
                    for file in files:
                        if file.endswith('.jpg') or file.endswith('.png'):
                            filenames.append(os.path.join(root, file))
                return filenames

def main():

    current_dir = os.getcwd()   
    parser = argparse.ArgumentParser(description='Tool for image resize')
    parser.add_argument('infile',
                        help='File for the resize')
    parser.add_argument('size',
                        type=int,
                        help='Image resizing scale factor')
    parser.add_argument('-o',
                        '--outfile',
                        default=current_dir,
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
