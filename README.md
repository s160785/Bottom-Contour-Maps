# Bottom-Contour-Maps
Finding the Bottom Edge in the Contour Maps.

## Pre-requisites:

- python >= 3.6
- cv2

## Installation
```
pip3 install opencv-python
```

## Intution:

Bottom edge in the contour maps can be extacted by getting the longest contour in the denoised binary image.

Steps involved:
> ### Convert the images to Gray Scale

> ### Denosing the image using fastNlMeansDenoising functionality

> ### Canny edge detection.

> ### Finding the cotours in the thresould edged image.

> ### Drawing the max length contour on the image.


## Running the Script

- Change the path of the input image

- Run the app.py

```
python app.py
```
