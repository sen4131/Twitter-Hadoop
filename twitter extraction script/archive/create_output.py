#!/usr/bin/python

import time

path = "/home/training/test/"
filename_prefix = "output"
filename_suffix = ".py"

currenttime = str(int(time.time()))

filename = path + filename_prefix + "_" + currenttime + filename_suffix

print(filename)

