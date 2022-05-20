#!/usr/bin/env python
# coding: utf-8

# # rgb2gray
# ## Converts all RGB images in a folder to grayscale
# Author - Ilan Valencius
# -*- coding: utf-8 -*-
"""
Converts a series of rgb files to grayscale according to [opencv conversion](https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html#cvtcolor)

Created on Jan 31 10:06:48 2022

@author: valencig
"""

# Import dependencies
import glob
import cv2
import os
from tqdm import tqdm

# Set parameters
img_folder = "INSERT" # Folder containing images (use '\\' AND absolute path)
file_ext = "*.tif" # File extension with regex: *.png for png files, *.tif for tiff files
save_folder = "INSERT" # Folder to save new grayscale images


filenames = glob.glob(img_folder+file_ext)

for file in tqdm(filenames):
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(save_folder+os.path.basename(file), gray)




