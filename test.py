import cv2
import numpy
import imutils
import math
import time

backSub = cv2.createBackgroundSubtractorKNN()


def show_webcam():
    cam = cv2.VideoCapture(0)
    i = 0
    max_dist = 0
    background = None
    while True:
        ret_val, img = cam.read()
        if (background is None or i == 0):
            time.sleep(.1)
            ret_val, img = cam.read()
            background = img

        # working on background segmentation
        #img = cv2.subtract(img,background)

        #some preprocessing stuff
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = backSub.apply(img)

        img = cv2.flip(img, 1)
        img = cv2.GaussianBlur(img, (25, 25), 0)


        thresh_value = 50

        thresh = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)[1]

        thresh = cv2.erode(thresh, None, iterations=2)

        thresh = cv2.dilate(thresh, None, iterations=2)

        #find contours
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        #put into color to display circles
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        if (len(cnts) != 0):
            c = max(cnts, key=cv2.contourArea)

            extLeft = tuple(c[c[:, :, 0].argmin()][0])
            extRight = tuple(c[c[:, :, 0].argmax()][0])
            extTop = tuple(c[c[:, :, 1].argmin()][0])
            extBot = tuple(c[c[:, :, 1].argmax()][0])
            cv2.drawContours(img, [c], -1, (0, 255, 255), 2)

            cv2.circle(img, extRight, 8, (0, 255, 0), -1)
            cv2.circle(img, extTop, 8, (255, 0, 0), -1)
            cv2.circle(img, extLeft, 8, (0, 0, 255), -1)
            cv2.circle(img, extBot, 8, (0, 127, 127), -1)



            dist = int(math.sqrt((extTop[0]-extRight[0])**2+(extTop[1]-extRight[1])**2))
            frac = dist/200

            # warning - this breaks your ears
            # osascript.osascript("set volume output volume " + str(frac*30))



        cv2.imshow('img', img)

        i += 1
        if i > 100:
            i = 0
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()
