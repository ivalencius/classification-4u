# -*- coding: utf-8 -*-
"""
Splits an image into a series of patches and saves them in a new directory.

Created on Mon Apr 11 10:25:32 2022

@author: valencig
"""

import numpy as np
from matplotlib import pyplot as plt
from patchify import patchify
import tifffile as tiff
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

save_path = 'INSERT'
image_path = 'INSERT'
patch_wind = 512 # creates patches of size patch_wind x patch_wind

Image.MAX_IMAGE_PIXELS = 933120000   
large_image = Image.open(image_path)     
large_image = np.array(large_image)
#plt.imshow(large_image)
height, width, _ = large_image.shape
from math import floor
large_image = large_image[:floor(height/patch_wind)*patch_wind, :floor(width/patch_wind)*patch_wind, :]
patches_img = patchify(large_image, (patch_wind,patch_wind,3), step=patch_wind)  #Step=patch_wind means no overlap

for i in range(patches_img.shape[0]):
    for j in range(patches_img.shape[1]):
        single_patch_img = Image.fromarray(patches_img[i,j,:,:].squeeze())
        single_patch_img.save(save_path + str(i)+'_'+str(j)+ ".png")
