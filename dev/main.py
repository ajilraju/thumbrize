#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:15:25 2019

@author: jerald
"""
def Run(argument):
    switcher = {
        1: "resize the image",
        2: "crop the image ",
        3: "reduce the resulution ",
        4: "resuze the size( compress)",
    }
    return switcher.get(argument, "this package is not suitable for your selected option try another")


if __name__ == "__main__":
    print("1.resize the image")
    print("2.crop the image")
    print("3.reduce the resulution")
    print("4.resuze the size( compress)")
    argument = int(input("enter your choise\n"))
    print (Run(argument))