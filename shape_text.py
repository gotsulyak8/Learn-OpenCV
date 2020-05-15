import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#img[:] = 255, 0, 0  # make it blue
#img[100:200, 200:300] = 255, 0, 0  # put blue square

# Draw a line
#cv2.line(img, (0, 0), (100, 400), (0, 255, 0), 3)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)  # heigth, width
# Draw a rectangle
cv2.rectangle(img, (0, 0), (200, 300), (0, 0, 255), cv2.FILLED)
# Draw a circle
cv2.circle(img, (400, 300), 40, (255, 0, 255), 3)
# Put a text
cv2.putText(img, 'OpenCV', (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (150, 151, 0), 2)

cv2.imshow('Box', img)
cv2.waitKey(0)