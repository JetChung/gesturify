import numpy as np
import cv2
import time


def get_gesture(gest1, gest2):
    if gest1 == "fist" and gest2 == "palm":
        print("closed")
    elif (gest1 == "palm" and gest2 == "fist"):
        print("open")
    else:
        pass

def show_webcam():
    fist = cv2.CascadeClassifier('fist.xml')
    palm = cv2.CascadeClassifier('palm.xml')

    gest1 = None #one frame ago
    gest2 = None #two frames ago

    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        img = cv2.GaussianBlur(img, (15, 15), 0)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        fist_detect = fist.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in fist_detect:
            img = cv2.rectangle(img, (x-50, y-50), (x + w+50, y + h+50), (255, 0, 0), 2)
            img = cv2.putText(img, 'fist', (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
            gest2 = gest1
            gest1 = "fist"



            roi = img[y:y + h, x:x + w]
        palm_detect = palm.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in palm_detect:
            img = cv2.rectangle(img, (x-50, y-150), (x + w+50, y + h+150), (255, 0, 0), 2)
            img = cv2.putText(img, 'palm', (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
            gest2 = gest1
            gest1 = "palm"

            roi = img[y:y + h, x:x + w]

        cv2.imshow("test", img)


        try:
            get_gesture(gest1, gest2)
        except:
            pass
        if cv2.waitKey(1) == 27:
            break


    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()


