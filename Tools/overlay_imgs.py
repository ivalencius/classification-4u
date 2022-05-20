# -*- coding: utf-8 -*-
"""
Overlays an image (such as a mask) over a base image

Created on Fri Apr 22 11:31:27 2022

@author: valencig
"""

from PIL import Image
import matplotlib.pyplot as plt
Image.MAX_IMAGE_PIXELS = 933120000   

base_img = Image.open('INSERT')
overlay_img = Image.open('INSERT)

# Make background pixels transparent
overlay_img = overlay_img.convert("RGBA")
datas = overlay_img.getdata()
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0: # For pixel value (0, 0, 0)
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)

overlay_img.putdata(newData)
# make image overlay

plt.imshow(base_img, interpolation=None)
plt.imshow(overlay_img, interpolation=None, alpha=0.5)
plt.show()