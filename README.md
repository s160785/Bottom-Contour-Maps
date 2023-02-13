# Bottom-Contour-Maps
Finding the Bottom Edge in the Contour Maps.



## Intution:

Bottom edge in the contour maps can be extacted by getting the longest contour in the denoised binary image.

Steps involved:
> ### Convert the images to Gray Scale

> ### Denosing the image using fastNlMeansDenoising functionality

> ### Canny edge detection.

> ### Finding the cotours in the thresould edged image.

> ### Drawing the max length contour on the image.
