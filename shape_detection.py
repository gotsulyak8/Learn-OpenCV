import numpy as np
import cv2


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 500:
            cv2.drawContours(img_copy, contour, -1, (255, 0, 0), 3)  # -1 to draw all contours
            perimeter = cv2.arcLength(contour, True)
            # print(perimeter)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            print(len(approx))
            corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if corners == 3:
                obj_type = 'Triangle'
            elif corners == 4:
                asp_ratio = w / float(h)
                if 0.95 < asp_ratio < 1.05:
                    obj_type = 'Square'
                else:
                    obj_type = 'Rectangle'
            elif corners == 5:
                obj_type = 'Pentagon'
            elif corners > 5:
                obj_type = 'Circle'
            else:
                obj_type = 'None'
            cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img_copy, obj_type, (x + (w // 2) - 10, y + (h // 2) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)


img = cv2.imread('images/**ANY_IMAGE**')
img = cv2.resize(img, (640, 480))
img_copy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 1)
canny = cv2.Canny(blurred, 50, 50)

get_contours(canny)

cv2.imshow('Image', img)
cv2.imshow('Gray', gray)
cv2.imshow('Blurred', blurred)
cv2.imshow('Canny', canny)
cv2.imshow('Contours', img_copy)
cv2.waitKey(0)
