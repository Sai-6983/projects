from ultralytics import YOLO
import cv2  #used for delay of image else result will close so we use cv2.waitKey(0)
model=YOLO('yolov8n.pt')
results=model('../images/3.jpg',show=True)
cv2.waitKey(0)