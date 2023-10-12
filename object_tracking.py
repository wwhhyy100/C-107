import cv2
import time
import math

#use crst to track

video = cv2.VideoCapture("bb3.mp4")

#Load Tracker
tracker = cv2.TrackerCSRT_create()

#Read the first frame of the video
returned, img = video.read()

#Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

#Initialise the tracker on the img and the box
tracker.init(img,bbox)

print(bbox)

while True:
    check,img = video.read() 

    #update the tracker on the img and bbox
    success,bbox=tracker.update(img)

    if success:
        drawBox(img,bbox)

    else:
        cv2.putText(img,"lost",(75,90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7,(0,0,255),2)

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"tracking",(75,90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7,(0,0,255),2)


    
video.release()
cv2.destroyALLwindows()



