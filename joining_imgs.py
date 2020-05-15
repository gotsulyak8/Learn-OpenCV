import numpy as np
import cv2

img = cv2.imread('images/**ANY_IMAGE**')

horizontal = np.hstack((img, img))
vertical = np.vstack((img, img))

cv2.imshow('Horizontal', horizontal)
cv2.imshow('Vertical', vertical)
cv2.waitKey(0)