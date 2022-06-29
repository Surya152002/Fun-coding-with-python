import numpy as np
import cv2
cascadeSCREEN="cars.xml"
video = "Enter the video location or name"

def detectCars(filename):
    rectangles = []
    cascade = cv2.CascadeClassifier(cascadeSCREEN)

    vc=cv2.VideoCapture(filename)

    if vc.isOpened():
        rval,frame =vc.read()
    else:
        rval = False
    while rval:
        rval,frame =vc.read()
        frameHeight,frameWidth,fdepth =frame.shape
    #Resize
    frame=cv2.resize(frame,(600,400))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detection
    cars=cascade.detectMultiScale(gray,1.3,3)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    #show result
    cv2.imshow("Outcome",frame)
    if cv2.waitKey(33) == ord("c"):
        break
vc.release()