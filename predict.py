<<<<<<< HEAD
import os
from ultralytics import YOLO
import cv2

# import numpy as np
VideoDir = os.path.join('.', 'Videos')
VideoPath =os.path.join(VideoDir, 'video5.mp4')
ModelPath = os.path.join('.', 'models', 'best.pt')
Model = YOLO(ModelPath)
threshold = 0.5 

ClassName = {0: 'Helmet',
             1: 'No Helmet'}

cap = cv2.VideoCapture(VideoPath)
while cap.isOpened():
    ret, Frame = cap.read()
    results = Model.predict(Frame)
    # results = result[0].boxes
    color = (255,255,255)
    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        print(boxes)
        classes = boxes.cls
        for idx,box in enumerate(boxes.xyxy):
            x1,y1,x2,y2 = box
            c1 = int(x1.item())
            c2 = int(y1.item())
            c3 = int(x2.item())
            c4 = int(y2.item())
            if(classes[idx] == 0):
                color = (255,0,0)
            else:
                color = (0,255,0)
            Frame = cv2.rectangle(Frame, (c1,c2), (c3,c4), color, thickness=2)
        
    # Frame = cv2.rectangle(Frame, (x1,y1), (x2,y2), (255,255,255), thickness=2)
    cv2.imshow("Frame",Frame)
    if(cv2.waitKey(0)):
        break

=======
import os
from ultralytics import YOLO
import cv2

# import numpy as np
VideoDir = os.path.join('.', 'Videos')
VideoPath =os.path.join(VideoDir, 'video5.mp4')
ModelPath = os.path.join('.', 'models', 'best.pt')
Model = YOLO(ModelPath)
threshold = 0.5 

ClassName = {0: 'Helmet',
             1: 'No Helmet'}

cap = cv2.VideoCapture(VideoPath)
while cap.isOpened():
    ret, Frame = cap.read()
    results = Model.predict(Frame)
    # results = result[0].boxes
    color = (255,255,255)
    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        print(boxes)
        classes = boxes.cls
        for idx,box in enumerate(boxes.xyxy):
            x1,y1,x2,y2 = box
            c1 = int(x1.item())
            c2 = int(y1.item())
            c3 = int(x2.item())
            c4 = int(y2.item())
            if(classes[idx] == 0):
                color = (255,0,0)
            else:
                color = (0,255,0)
            Frame = cv2.rectangle(Frame, (c1,c2), (c3,c4), color, thickness=2)
        
    # Frame = cv2.rectangle(Frame, (x1,y1), (x2,y2), (255,255,255), thickness=2)
    cv2.imshow("Frame",Frame)
    if(cv2.waitKey(0)):
        break

>>>>>>> ed433af (initial commit)
cv2.destroyAllWindows()    