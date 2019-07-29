import cv2
import numpy as np
import pickle
import os
import time
# import database

face_recognizer = cv2.face.LBPHFaceRecognizer_create();
face_detect =  cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml');

labels_array = {'name':0};
face_recognizer.read('data/trainner.yml');
with open('data/label.pickle','rb') as f:
	labels_= pickle.load(f);
	labels_array = {v:k for k,v in labels_.items()}

cap = cv2.VideoCapture(0);

name = '';

while (True):
	ret, frame = cap.read();
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
	faces = face_detect.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5);
	for (x,y,w,h) in faces:
		roi_gray = gray[y:y+h,x:x+w];
		roi_color = frame[y:y+h,x:x+w];
		# cv2.imshow('face',roi_gray);
		id_,conf = face_recognizer.predict(roi_gray);
		if(conf >= 70) & (conf <= 100): #1 & (labels_array[id_]!= name):
			print(labels_array[id_],conf);
			name = labels_array[id_];
			width = x+w+10;
			height = y+h+20;
			color =(0,200,0); #BGR
			stroke = 2; #border weight
			cv2.rectangle(frame,(x-10,y-50),(width,height),color,stroke);
			text = 'Are you '+labels_array[id_]+'?';
			name = labels_array[id_];
			cv2.putText(frame,text,(x-100,y-70),cv2.FONT_HERSHEY_SIMPLEX,1,(250,0,0),2,cv2.LINE_AA); 
	cv2.imshow('webcam',frame)
	if cv2.waitKey(20) & 0xff == ord('y'):
		# database.checkin(name);
		break;

cap.release();
cv2.destroyAllWindows();