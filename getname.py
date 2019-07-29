import cv2
import numpy as np
import pickle
import os

face_recognizer = cv2.face.LBPHFaceRecognizer_create();
face_detect =   cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml');

labels_array = {'name':0};
face_recognizer.read('data/trainner.yml');
with open('data/label.pickle','rb') as f:
	labels_= pickle.load(f);
	labels_array = {v:k for k,v in labels_.items()}

def name(frame,faces):
	name = '';
	for (x,y,w,h) in faces:
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
		roi_gray = gray[y:y+h,x:x+w];
		id_,conf = face_recognizer.predict(roi_gray);
		if(conf >= 70) & (conf <= 100): #1 & (labels_array[id_]!= name):
			# print(labels_array[id_],conf);
			name = labels_array[id_];
			text = labels_array[id_]+'?';
			name = labels_array[id_];
			cv2.putText(frame,text,(x-50,y-70),cv2.FONT_HERSHEY_SIMPLEX,1,(250,0,0),2,cv2.LINE_AA);
	if(name is not ''):
		return name;