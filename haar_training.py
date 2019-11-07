import numpy as np
import cv2
import time
import osascript


def get_gesture(gest1, gest2):
    if gest1 == "fist" and gest2 == "palm":
        osascript.osascript("""
        tell application "Tunify"
	        pause
        end tell
        """)


    elif (gest1 == "palm" and gest2 == "fist"):
        osascript.osascript("""
            tell application "Tunify"
        	    play
            end tell
            """)

    else:
        return None
def get_control(x_0, y_0, x_1, y_1):

    if (x_1 > 300 and x_1 < 900):
        if (x_0 < 300):
            print ("track back")
        if (x_0 < 300):
            print("track forward")

    if (y_1 > 200 and y_1 < 500):
        if (y_0 < 200):
            print ("volume up")
        if (y_0 < 500):
            print("volume down ")


def show_webcam():
    fist = cv2.CascadeClassifier('fist.xml')
    palm = cv2.CascadeClassifier('palm.xml')

    gest1 = None # one frame ago
    gest2 = None # two frames ago

    x_0 = None
    y_0 = None
    x_1 = None
    y_1 = None

    time0 = 0

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
            time0 = 5
            x_1 = x_0
            x_0 = x
            y_1 = y_0
            y_0 = y
            print("fist: ({}, {})".format(x,y))



            roi = img[y:y + h, x:x + w]
        palm_detect = palm.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in palm_detect:
            img = cv2.rectangle(img, (x-50, y-150), (x + w+50, y + h+150), (255, 0, 0), 2)
            img = cv2.putText(img, 'palm', (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
            gest2 = gest1
            gest1 = "palm"
            time0 = 5
            x_1 = x_0
            x_0 = x
            y_1 = y_0
            y_0 = y
            print("palm: ({}, {})".format(x,y))


            roi = img[y:y + h, x:x + w]


        if time0 <= 0:
            x_1 = None
            y_1 = None

            gest1 = None
            gest2 = None

        time0 -= 1


        get_gesture(gest1, gest2)
        get_control(x_0,y_0,x_1, y_1)

        if cv2.waitKey(1) == 27:
            break
        cv2.imshow("test", img)
        time.sleep(0.1)

    cv2.destroyAllWindows()



def main():
    show_webcam()


if __name__ == '__main__':
    main()


