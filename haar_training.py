import numpy as np
import cv2



def show_webcam():
    fist = cv2.CascadeClassifier('aGest.xml')
    palm = cv2.CascadeClassifier('palm.xml')
    aGest = cv2.CascadeClassifier('aGest.xml')
    closed_frontal_palm = cv2.CascadeClassifier('closed_frontal_palm.xml')

    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detect = fist.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in detect:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)



            img = cv2.putText(img, 'palm',
                              (x,y+h),
                              cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                              (255,0,0),
                        2)

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
