import cv2
Fcascade = cv2.CascadeClassifier("face-default.xml")
cap =cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting to Gray scale
    faces = Fcascade.detectMultiScale(gray,1.1,4) # Detect Faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # Drawing rectangle on faces
    #Displaying Result
    cv2.imshow('OUTCOME',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
