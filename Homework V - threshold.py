"""
Homework V - Session 11

Take a picture of a scene. Then, without moving the camera, put
a coffee cup in the scene and take a second picture. Load these
images and convert both to 8-bit grayscale images.
a. Take the absolute value of their difference. Display the result,
which should look like a noisy mask of a coffee mug.
b. Do a binary threshold of the resulting image using a level
that preserves most of the coffee mug but removes some of
the noise. Display the result. The “on” values should be set to
255.

Use your own pictures!!
"""

import cv2
import numpy as np

img_a = cv2.imread("./assets/cup1.jpg")
img_b = cv2.imread("./assets/cup2.jpg")

img_a_gray = cv2.cvtColor(img_a, cv2.COLOR_BGR2GRAY)
img_b_gray = cv2.cvtColor(img_b, cv2.COLOR_BGR2GRAY)
diff = np.abs(img_a_gray - img_b_gray)

cv2.imshow("diff", diff)
_, thresh = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholded Image', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()