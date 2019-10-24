import cv2
import numpy as np
import imutils
import osascript
import math
import time

fgbg = cv2.createBackgroundSubtractorMOG2()
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

def show_webcam():
    cam = cv2.VideoCapture(0)
    i = 0
    max_dist = 0
    background = None
    while True:
        ret_val, img = cam.read()
        if (background is None):
            time.sleep(.1)
            ret_val, img = cam.read()
            background = img

        # working on background segmentation
        #img = cv2.subtract(img,background)

        #some preprocessing stuff
        #img = cv2.subtract(img,background)
        img = cv2.flip(img, 1)
        #img = cv2.GaussianBlur(img, (15, 15), 0)

        frame = imutils.resize(img, width=400)
        converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)

        # apply a series of erosions and dilations to the mask
        # using an elliptical kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        skinMask = cv2.erode(skinMask, kernel, iterations=2)
        skinMask = cv2.dilate(skinMask, kernel, iterations=2)

        # blur the mask to help remove noise, then apply the
        # mask to the frame
        skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
        skin = cv2.bitwise_and(frame, frame, mask=skinMask)

        # show the skin in the image along with the mask
        cv2.imshow("images", np.hstack([frame, skin]))


        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()
