import numpy as np
import cv2

img = cv2.imread('images/**ANY_IMAGE**')
kernel = np.ones((5, 5), np.uint8)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
canny = cv2.Canny(gray, 100, 100)
dilation = cv2.dilate(canny, kernel, iterations=1)
eroded = cv2.erode(dilation, kernel, iterations=1)

cv2.imshow('Marushchak', gray)
cv2.imshow('Blurred image', blurred)
cv2.imshow('Canny image', canny)
cv2.imshow('Dilated image', dilation)
cv2.imshow('Eroded image', eroded)
cv2.waitKey(0)