import numpy as np
import cv2
import handy

global cam, hist, fist, palm
cam = cv2.VideoCapture(0)

hist = handy.capture_histogram(source=0)
fist = cv2.CascadeClassifier('fist.xml')
palm = cv2.CascadeClassifier('palm.xml')

def mse(imageA, imageB):

    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def show_webcam():
    while True:
        ret_val, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        fist_detect = fist.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in fist_detect:
            img = cv2.rectangle(img, (x - 50, y - 50), (x + w + 50, y + h + 50), (255, 255, 0), 2)
            img = cv2.putText(img, 'fist', (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            roi = img[y-150:y + h+150, x-50:x + w+50]

            try:
                hand = handy.detect_hand(roi, hist)
                for fingertip in hand.fingertips:
                    fingertip = fingertip[0]+x-50, fingertip[1]+y-50
                    cv2.circle(roi, fingertip, 5, (0, 0, 255), -1)
                    cv2.imshow("Test", img)

            except:
                pass

            #img = roi(img, a)

        palm_detect = palm.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in palm_detect:
            img = cv2.rectangle(img, (x - 50, y - 150), (x + w + 50, y + h + 150), (255, 255, 0), 2)
            img = cv2.putText(img, 'palm', (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            #a = np.array([[x, 10], [100, 10], [100, 100], [10, 100]], dtype=np.int32)

            #img = roi(img, a)



        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()


