import numpy as np
import cv2
import time


def show_webcam():
    fist = cv2.CascadeClassifier('fist.xml')
    palm = cv2.CascadeClassifier('palm.xml')
    fists = 0
    palms = 0

    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        fist_detect = fist.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in fist_detect:
            img = cv2.rectangle(img, (x-50, y-50), (x + w+50, y + h+50), (255, 0, 0), 2)
            img = cv2.putText(img, 'fist', (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
            fists+=1
            print(fists)


            roi = img[y:y + h, x:x + w]
        palm_detect = palm.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in palm_detect:
            img = cv2.rectangle(img, (x-50, y-150), (x + w+50, y + h+150), (255, 0, 0), 2)
            img = cv2.putText(img, 'palm', (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
            palms+=1

            roi = img[y:y + h, x:x + w]

        cv2.imshow("test", img)




        if cv2.waitKey(1) == 27:
            break

        time.sleep(0.1)

    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()
