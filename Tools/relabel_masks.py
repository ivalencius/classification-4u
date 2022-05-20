# -*- coding: utf-8 -*-
"""
Relabels a series of grayscale masks

Created on Wed Mar 30 11:35:18 2022

@author: valencig
"""


import os
import glob
import cv2
from tqdm import tqdm
import matplotlib.pyplot as plt
import random
import numpy as np

# Set parameters
mask_folder = 'INSERT'
img_files = glob.glob(mask_folder+'*.png')
write_folder = 'INSERT'


print('Processing %d files'%len(img_files))

for i in tqdm(range(len(img_files))):
    file = img_files[i]
    img = cv2.imread(os.path.join(mask_folder, file), cv2.IMREAD_GRAYSCALE)
    img_relabel = np.zeros_like(img)

    # In new mask, previous label of x is now y
    # The rest is nodata --> 0
    img_relabel[img == x] = y # Repeat code block for as many classes as necessary

    cv2.imwrite(os.path.join(write_folder,os.path.basename(file)),img_relabel)