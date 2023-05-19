"""
Homework II - Session 4

Using only opencv and numpy, create a “paint” application that:
• Creates an empty canvas of 800 x 800 pixels with a gray (127, 127, 127)
background and shows it to the user when the script is executed
• Allows the user to draw with the mouse (in a different color) clears the
canvas by pressing key ‘c’
• Saves the image to a .png image file when the user presses the key ‘s’
"""

import cv2
import numpy as np

painting = np.ones((800, 800, 3), dtype=np.uint8)*127 # grey background 
color = (0, 255, 0) # green color to draw with

ix,iy = -1,-1 # initial mouse position

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(painting,(x,y),30,color,-1)


cv2.namedWindow('painting')
cv2.setMouseCallback('painting', draw_circle())

while True:
    cv2.imshow('painting', painting)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        painting = np.ones((800, 800, 3), dtype=np.uint8)*127 # reset to grey background
    if key == ord('s'):
        cv2.imwrite('painting.png', painting) # save to png file
        break
    if key == ord('q'):
        break

cv2.destroyAllWindows()