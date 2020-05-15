import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height
cap.set(10, 50)  # Brightness

colors = [[27, 179, 142, 255, 0, 255],
          [31, 179, 128, 255, 176, 255],
          [38, 179, 65, 255, 255, 255]]


def empty(a):
    pass


cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
cv2.createTrackbar('Hue min','TrackBars',0, 179, empty)
cv2.createTrackbar('Hue max','TrackBars',179, 179, empty)
cv2.createTrackbar('Sat min','TrackBars',0, 255, empty)
cv2.createTrackbar('Sat max','TrackBars',36, 255, empty)
cv2.createTrackbar('Val min','TrackBars',175, 255, empty)
cv2.createTrackbar('Val max','TrackBars',255, 255, empty)

while True:
    _, frame = cap.read()  # True/False, frame
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('Hue min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Val min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val max', 'TrackBars')

    lower = np.array(h_min, s_min, v_min)
    upper = np.array(h_max, s_max, v_max)
    mask = cv2.inRange(frame_hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Maks', mask)
    cv2.imshow('Picker', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to exit
        break