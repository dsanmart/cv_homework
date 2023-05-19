"""
Homework VI - Session 13

Load an image containing a side view of a bicycle with
clear lines and circles.
Use the Hough line and Hough circle functions in
OpenCV and detect the lines and circles on the bike.
"""

import cv2
import numpy as np

# Load the image
img = cv2.imread("./assets/bike.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Draw lines
edges = cv2.Canny(gray, 5, 150, apertureSize=3, L2gradient=True)
lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)
if lines is not None:
    for line in lines:
        # rho is distance from origin to line
        # theta is angle from origin to line
        rho, theta = line[0]
        a, b = np.cos(theta), np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Draw circles
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 0)
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 10, param1=100, param2=40, minRadius=1, maxRadius=120)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        cv2.circle(img, (circle[0], circle[1]), circle[2], (255, 0, 255), 3) # draw circle

cv2.imshow("Bike Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()