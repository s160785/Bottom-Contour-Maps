import cv2
import numpy as np

# Loading the Image
image = cv2.imread('19.BMP')
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Denoising the image 
denoised = cv2.fastNlMeansDenoising(gray, None,40,13,31)

# Canny edge detection
canny = cv2.Canny(denoised, 30, 200)

# Thresholding the image.
_, threshold = cv2.threshold(canny, 127, 255, cv2.THRESH_BINARY)

# Finding Contours on the Binary image
contours, hierarchy = cv2.findContours(threshold,
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Threshold image: ', threshold)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

# Finding the max length in the Contours found
cnt = [cv2.arcLength(cnt,True) for cnt in contours]
a = contours[cnt.index(max(cnt))]

# Drawing the contour on the image
cv2.drawContours(image, [a], 0, (0, 255, 0), 3)
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
