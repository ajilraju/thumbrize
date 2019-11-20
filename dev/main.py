#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:15:25 2019

@author: jerald
"""
from Resize import resize
p1=resize.ResizeFile()
def Run(argument):
    if(argument==1):
         p1.getValue()
    elif(argument!=1):
        print("this package is under maintenance")

if __name__ == "__main__":
    print("1.resize the image")
    print("2.crop the image")
    print("3.reduce the resulution")
    print("4.resuze the size( compress)")
    argument = int(input("enter your choise\n"))
    Run(argument)