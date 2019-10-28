import numpy as np
import cv2



def show_webcam():
    fist = cv2.CascadeClassifier('fist.xml')
    left = cv2.CascadeClassifier('left.xml')
    right = cv2.CascadeClassifier('right.xml')
    lpalm = cv2.CascadeClassifier('lpalm.xml')
    rpalm = cv2.CascadeClassifier('rpalm.xml')

    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        fist = fist.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in fist:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
        left = left.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in left:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
        right = right.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in right:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]


        cv2.imshow("test", img)


        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()
