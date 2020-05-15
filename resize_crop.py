import numpy as np
import cv2

# Resizing
img = cv2.imread('images/**ANY_IMAGE**')
print(img.shape)
resized = cv2.resize(img, (300, 150))  # width, heigth
print(resized.shape)

# Cropping
cropped = img[0:200, 300:700]  # height, width

cv2.imshow('Image', img)
cv2.imshow('Resized', resized)
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)