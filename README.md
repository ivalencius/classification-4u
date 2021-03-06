# classification-4u

## Overview
This project aims to provide an out of the box solution for semantic segmentation tasks, namely land-use classification from orthophotos. Both notebooks are designed to be intuitive for those without deep learning experience. Please use [2D_semantic.ipynb](https://github.com/ivalencius/classification-4u/blob/main/2D_semantic.ipynb) for grayscale images and [3D_semantic.ipynb](https://github.com/ivalencius/classification-4u/blob/main/3D_semantic.ipynb) for RGB or other three channel imagery (make a copy of either in your drive before using). For other numbers of bands, please edit the 2D file as the file already has support for non-RGB data (see [segmentation models: training with non-rgb data](https://segmentation-models.readthedocs.io/en/latest/tutorial.html#training-with-non-rgb-data)). [Tools](https://github.com/ivalencius/classification-4u/tree/main/Tools) contains a series of helper files that can automate various dataset preparation tasks. 

## Some useful orthophoto datasets
* [LoveDA: A Remote Sensing Land-Cover Dataset for Domain Adaptive Semantic Segmentation](https://github.com/Junjue-Wang/LoveDA)
* [LandCover.ai](https://landcover.ai.linuxpolska.com/)
* [SpaceNet](https://spacenet.ai/)
* [DeepGlobe](http://deepglobe.org/index.html)
* [ZurichSummer](https://sites.google.com/site/michelevolpiresearch/data/zurich-dataset)

## For geology folks
* [colab_zirc_dims](https://github.com/MCSitar/colab_zirc_dims)

More resources → [awesome semantic segmenation](https://github.com/mrgloom/awesome-semantic-segmentation)

## Acknowledgements
All notebooks are adapted from [ZeroCostDL4Mic](https://github.com/HenriquesLab/ZeroCostDL4Mic). Models implemented are from [segmentation models](https://github.com/qubvel/segmentation_models).
