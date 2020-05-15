import numpy as np
import cv2

img = cv2.imread('images/**ANY_IMAGE**')
width, height = 250, 350
pts1 = np.float32([[505, 157], [583, 261], [340, 225], [411, 342]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Cards', img)
cv2.imshow('Output', output)
cv2.waitKey(0)