import cv2
import numpy as np

cap = cv2.VideoCapture("C:\Users\KOREA\Desktop\ddd.mp4")


def roi_mask(img, color=[255]):
    mask = np.zeros_like(img)
    roi_corners = np.array(
        [[(200, 700), (800, 700), (600, 600), (300, 600)]], dtype=np.int32)
    cv2.fillPoly(mask, roi_corners, color)
    roi = cv2.bitwise_and(img, mask)
    return roi


while True:

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    roi_img = roi_mask(edges)

    minLineLength = 100
    maxLienGap = 10

    lines = cv2.HoughLinesP(roi_img, 1, np.pi/90, 30,
                            minLineLength, maxLienGap)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 10)

    cv2.imshow('test', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
