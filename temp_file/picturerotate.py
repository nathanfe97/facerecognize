import os
import cv2
import numpy as np
import imutils

BASE_DIR = os.path.dirname(os.path.abspath(__file__));
img_dir =  os.path.join(BASE_DIR, 'images-scan');

face_detect = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml');

for root,dirs,files in os.walk(img_dir):
	for file in files:
		if file.endswith('jpg'):
			path = os.path.join(root,file)
			img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
			# dim = img.shape;
			# height = img.shape[0]
			# width = img.shape[1]
			# img = cv2.resize(img, (300, 400))
			# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
			# faces = face_detect.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5);
			faces = ();
			while (faces is ()):
				# img = cv2.resize(img, (300, 400))
				gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
				faces = face_detect.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5);
				if faces is ():
					img = imutils.rotate_bound(img, 90);
					cv2.imwrite(path,img);
			print(faces);
