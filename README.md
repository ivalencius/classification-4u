# classification-4u

## Overview
This project aims to provide an out of the box solution for semantic segmentation tasks, namely land-use classification from orthophotos. Both notebooks are designed to be intuitive for those without deep learning experience. Please use [2D_semantic.ipynb](https://github.com/ivalencius/classification-4u/blob/main/2D_semantic.ipynb) for grayscale images and [3D_semantic.ipynb](https://github.com/ivalencius/classification-4u/blob/main/3D_semantic.ipynb) for RGB or other three channel imagery. For other numbers of bands, please edit the 2D file as the file already has support for non-RGB data (see [segmentation models: training with non-rgb data](https://segmentation-models.readthedocs.io/en/latest/tutorial.html#training-with-non-rgb-data)).

## Datasets
* [LoveDA: A Remote Sensing Land-Cover Dataset for Domain Adaptive Semantic Segmentation](https://github.com/Junjue-Wang/LoveDA)
* [LandCover.ai](https://landcover.ai.linuxpolska.com/)

## Acknowledgements
All notebooks are adapted from [ZeroCostDL4Mic](https://github.com/HenriquesLab/ZeroCostDL4Mic). Models implemented are from [segmentation models](https://github.com/qubvel/segmentation_models).
