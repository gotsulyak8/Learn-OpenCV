import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)  # Height
cap.set(10, 50)  # Brightness

colors = [[27, 142, 0, 179, 255, 255],
          [31, 128, 176, 179, 255, 255],
          [38, 65, 255, 179, 255, 255]]

color_values = [[0, 255, 255],  # BGR format
                [255, 0, 0],
                [0, 255, 0]]

points = []  # [x, y, colorID]


def find_color(img, colors, color_values):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points = []
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(hsv, lower, upper)
        x, y = get_contours(mask)
        cv2.circle(frame_result, (x, y), 10, color_values[count], cv2.FILLED)
        if x != 0 and y != 0:
          new_points.append([x, y, count])
        count += 1
    return new_points


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 500:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y


def draw_on_canvas(points, color_values):
    for point in points:
        cv2.circle(frame_result, (point[0], point[1]), 10, color_values[point[2]], cv2.FILLED)


while True:
    _, frame = cap.read()
    frame_result = frame.copy()
    new_points = find_color(frame, colors, color_values)
    if len(new_points) != 0:
        for point in new_points:
            points.append(point)
    if len(points) != 0:
        draw_on_canvas(points, color_values)
    cv2.imshow('Cam window', frame_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to exit
        break
