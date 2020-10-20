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
    while True:
        ret_val, img = cam.read()
        gray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        ret, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY_INV)

        cv2.imshow("test", thresh)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()
