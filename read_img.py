import cv2

# For image:

#img = cv2.imread('images/opencv_logo.png')
#cv2.imshow('Image window', img)
#cv2.waitKey(0)

# For web cam:

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height
cap.set(10, 100)  # Brightness

while True:
    successes, frame = cap.read()  # True/False, frame
    cv2.imshow('Cam window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to exit
        break
