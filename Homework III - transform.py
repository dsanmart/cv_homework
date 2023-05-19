"""
Homework III - Session 5

Write a python script that takes as inputs:
-The 2D coordinates of the top left corner of a square
-The length of the square side

Using only OpenCV and Numpy plot any square defined by the
inputs and also plot arbitrary transformations of the square of
the following types:
-Translation
-Euclidean
-Affine
-Homography
"""

import cv2
import numpy as np

def draw_squares(x, y, length):
    # 2D translation matrix (2x3)
    translation = np.float32([[1, 0, 50], [0, 1, 100]])

    # rigid, euclidean transformation matrix (2x3) describing the translation, rotation and scaling of the square
    euclidean = cv2.getRotationMatrix2D((x + 80, y + 100), 45, 0.7)

    # Affine transformation matrix (2x3) preserving parallelism
    affine = np.float32([[0.5, 0.5, 100], [-0.5, 0.5, 200]])

    # Homography/projective transformation matrix (straight lines are preserved)
    h_x = np.float32([[x, y], [x+150, y], [x, y+150]])
    h_y = np.float32([[x+150, y+150], [x+100, y+50], [x+50, y+150]])
    homography = cv2.getAffineTransform(h_x, h_y)

    transformations = {'Translation': translation, 'Euclidean': euclidean, 'Affine': affine, 'Homography': homography}

    # Create a black canvas to plot the square and its transformations
    canvas = np.zeros((500, 500), dtype=np.uint8)

    # Draw the original square on the canvas
    cv2.rectangle(canvas, (x, y), (x+length, y+length), 255, -1)

    cv2.namedWindow('canvas')
    cv2.imshow('Original Square', canvas)
    key = cv2.waitKey(0)

    for transformation in transformations.keys():
        # Apply the transformations and draw the resulting squares on the canvas
        canvas = cv2.warpAffine(canvas, transformations[transformation], (500, 500))
        cv2.imshow(transformation, canvas)
        while not cv2.waitKey(0):
            pass # wait for any key to be pressed to continue
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    #x, y, length = 100, 100, 200 # 2D coords of the top-left corner of the square and length of the square side
    x = input('Enter the x coordinate of the top-left corner of the square: ')
    y = input('Enter the y coordinate of the top-left corner of the square: ')
    length = input('Enter the length of the square side: ')
    x, y, length = int(x), int(y), int(length)
    if x <= 0 or y <= 0 or length <= 0:
        raise ValueError('The coordinates and the length of the square must be positive integers')
    elif x + length > 500 or y + length > 500:
        raise ValueError('The square must be contained in a 500x500 canvas')
    else:
        print("Drawing the square, press 'space' to see its transformations, press 'q' to quit")
        draw_squares(x, y, length)