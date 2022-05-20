# -*- coding: utf-8 -*-
"""
Determines the Unique values and counts across all images in a directory
-> Useful for confirming the number of classes/creating class_weight dictionary

Created on Fri Feb 18 10:06:48 2022

@author: valencig
"""
import os
import glob
import cv2
import numpy as np
from tqdm import tqdm
import pandas as pd

# Set parameters
img_folder = 'F:\\Snyder_UNet_spring_2022\\UNet_data\\LoveDa\\Train\\base_imgs\\urban_masks_train\\'
#img_file_ext = ''
img_files = glob.glob(img_folder+'*.png')

print('Processing %d files'%len(img_files))

# Dataframe to store results
df = pd.DataFrame(columns=['Values','Counts'])

for i in tqdm(range(len(img_files))):
    file = img_files[i]
    img = cv2.imread(os.path.join(img_folder, file), cv2.IMREAD_GRAYSCALE)
    vals, counts = np.unique(img, return_counts=True)
    for i in range(len(vals)):
        if vals[i] is None:
            pass
        if vals[i] in df.values:
            df.loc[df['Values']==vals[i],'Counts'] += counts[i]
        else:
            df = df.append({'Values':vals[i], 'Counts':counts[i]},
                           ignore_index = True)
    
df.to_csv(img_folder+'00_unique_counts.csv',index=False)