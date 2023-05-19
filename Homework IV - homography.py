"""
Homework IV - Session 7

Given three images of a window taken from three different viewpoints,
a, b and c, obtain the homography matrices Hab and Hbc using the least
squares method. You can define correspondences manually.

Use numpy for matrix multiplication, transposition and inversion, other
methods are not accepted for obtaining the homography matrices.

Then compute a view equivalent to c, using only image a and the
homographies previously computed.

Every student should use his/her own photos!
No images downloaded from the internet are allowed.
"""

import cv2
import numpy as np

# Load the three images
img_a = cv2.imread("./assets/window2.jpg")
img_b = cv2.imread("./assets/window1.jpg")
img_c = cv2.imread("./assets/window3.jpg")

# Create a dictionary to store the images and the points selected by the user
images = {"image_a": img_a, "image_b": img_b, "image_c": img_c}
points = {"image_a": [], "image_b": [], "image_c": []}

# Some hardcoded points for testing
"""points = {'image_b': [(1287, 2570), (1210, 574), (1707, 779), (1713, 2873)], 
          'image_a': [(990, 3286), (943, 544), (2112, 597), (2133, 3182)], 
          'image_c': [(976, 2274), (1142, 355), (1969, 557), (1965, 2812)]}"""
# points = {"image_a": np.array(), "image_b": np.array(), "image_c": np.array()}

# mouse callback function
def click_event(event, x, y, flags, param):
    image_key, _ = param
    if event == cv2.EVENT_LBUTTONDOWN:
        points[image_key].append((x, y))

for image_key in images.keys():
    # create windows to show images
    cv2.namedWindow(image_key)

    # set mouse callback function for corresponding window clicks
    cv2.setMouseCallback(image_key, click_event, param=[image_key, images[image_key]])

    while True:
        cv2.imshow(image_key, images[image_key])
        key = cv2.waitKey(1)
        # exit loop if all points have been selected or q is pressed
        if len(points[image_key]) >= 4 or key == ord('q'):
            break
            

print(points)

# Compute the homography matrices using the least squares method
def homography_matrix(pts1, pts2):
    A = []
    for i in range(4):
        x, y = pts2[i]
        xp, yp = pts1[i]
        A.append([x, y, 1, 0, 0, 0, -xp*x, -xp*y, -xp])
        A.append([0, 0, 0, x, y, 1, -yp*x, -yp*y, -yp])
    A = np.array(A)
    U, S, Vt = np.linalg.svd(A)
    L = Vt[-1,:] / Vt[-1,-1]
    H = L.reshape(3, 3)
    return H

# Compute Hab and Hbc
Hab = homography_matrix(points["image_a"], points["image_b"])
Hbc = homography_matrix(points["image_b"], points["image_c"])

# Project image c onto the same plane as image a
# The view equivalent to c, using only image a and the homographies previously computed
Hab_inv = np.linalg.inv(Hab)
H_tot = np.dot(Hbc, Hab_inv)
im_out = cv2.warpPerspective(img_a, H_tot, (img_c.shape[1], img_c.shape[0]))

cv2.imshow('Output', im_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
