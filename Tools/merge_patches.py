# -*- coding: utf-8 -*-
"""
Merges patches created from extract_patches.py

Created on Mon Apr 11 10:30:56 2022

@author: valencig
"""

import numpy as np
from PIL import Image
from glob import glob
import os
import matplotlib.pyplot as plt
from tqdm import tqdm
Image.MAX_IMAGE_PIXELS = 933120000   
save_path = 'INSERT'
read_path = 'INSERT'
patch_sz = (512, 512)

# Get size of patches
file_list = glob(read_path+'*.png')
# Index of last file (+1 to each dim if indexes start at 0,0)
# Analagous to number of patches in y and x direction
ind = (16, 30)
img_sz = (patch_sz[0]*ind[0], patch_sz[1]*ind[1]) # add third dimension for 3+ channel images


save_arr = np.zeros(img_sz, dtype=np.uint)
for i in tqdm(range(len(file_list))):
    file = file_list[i]
    img = Image.open(file)
    im = np.array(img)
    name_no_ext = os.path.splitext(os.path.basename(file))[0]
    
    # Get row and column of patch
    r, c = name_no_ext.split('_')
    r = int(r)*patch_sz[0]
    c = int(c)*patch_sz[0]
    
    # Add patch in correct location
    save_arr[r:r+patch_sz[0], c:c+patch_sz[1], :] = im

        
#plt.imshow(save_arr)

reconstructed_image = Image.fromarray(save_arr.astype(np.uint8))

reconstructed_image.save(os.path.join(save_path, 'merged.png'))

