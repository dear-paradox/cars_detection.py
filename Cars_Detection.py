# cars_detection.py

import cv2
# choose your classifier path and sample video path 
# Note : this path example for Windows system if may you're using mac os or linux os check your path of....
car_cascade = cv2.CascadeClassifier(r"C:\\User\\SANJAY\\Downloads\\cars.xml")
cap = cv2.VideoCapture(r"C:\\User\\SANJAY\\Downloads\\vb.mp4")

while True:
    ret,frame = cap.read()
    gary = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,9)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x+y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("car_detection",frame)
    if cv2.waitKey(33) == 27:
        break
cap.release()
cv2.destroyAllWindows()
