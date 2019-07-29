import cv2
import numpy as np


face_detect =   cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml');

def face(frame):
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
	faces = face_detect.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5);
	for x,y,w,h in faces:
		width = x+w+10;
		height = y+h+20;
		color =(0,200,0);#BGR
		stroke = 2;
		cv2.rectangle(frame,(x-10,y-50),(width,height),color,stroke);
	return faces;

