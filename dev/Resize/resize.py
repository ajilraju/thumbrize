#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:22:55 2019

@author: jerald
"""
import os
from PIL import Image
# resize the image
class ResizeFile:
    
    def __init__(self):
        print("Resize File is ready")

    def getValue(self):
        #filePath,resizeFactor
        print("enter the file path")
        filePath=input("File path") 
        print("enter the resize factor")
        resizeFactor=input("resize factor") 
        self.filePath=filePath
        self.resizeFactor=resizeFactor
        print(resizeFactor)
        ap=Image(filename='/home/jerald/Pictures/one.jpg')
        ap._show()
        
