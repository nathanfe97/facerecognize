import cv2
import numpy as np
import pickle
import os
import time


face_recognizer = cv2.face.LBPHFaceRecognizer_create();
face_detect =   cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml');

labels_array = {'name':0};
face_recognizer.read('data/trainner.yml');
with open('data/label.pickle','rb') as f:
	labels_= pickle.load(f);
	labels_array = {v:k for k,v in labels_.items()}

BASE_DIR = os.path.dirname(os.path.abspath(__file__));
img_dir =  os.path.join(BASE_DIR, 'images-scan');
for root,dirs,files in os.walk(img_dir):
	for file in files:
		if file.endswith('jpg'):
			path = os.path.join(root,file)
			img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
			img_show = cv2.imread(path,1)
			img_show = cv2.resize(img_show, (300, 400))
			img = cv2.resize(img, (300, 400))
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
			faces = face_detect.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5);
			for (x,y,w,h) in faces:
				roi_gray = gray[y:y+h,x:x+w];
				id_,conf = face_recognizer.predict(roi_gray);
				if(conf >= 70) & (conf <= 100): #1 & (labels_array[id_]!= name):
					print(labels_array[id_],conf);
					cv2.rectangle(img_show,(x-10,y-50),(x+w,y+h),(255,0,0),2);
					cv2.putText(img_show,labels_array[id_],(x-30,y+h+30),cv2.FONT_HERSHEY_SIMPLEX,1,(250,0,0),2,cv2.LINE_AA);
				else:
					print("can't find a face on this picture");
			cv2.imshow('face',img_show);
			cv2.waitKey(0);
			cv2.destroyAllWindows();
