import cv2
import os
import numpy as np
from PIL import Image


face_detect =   cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml');

cap = cv2.VideoCapture(0);



while True:
	ret, frame = cap.read();
	# cv2.imwrite('test',frame);
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
	faces = face_detect.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=5);
	# print(faces);
	for x,y,w,h in faces:
		width = x+w+10;
		height = y+h+20;
		color =(0,200,0);#BGR
		stroke = 2;
		cv2.rectangle(frame,(x-10,y-50),(width,height),color,stroke);
	cv2.imshow('ok',frame);
	cv2.imwrite('images-temp/example.jpg',frame);
	pil_image = Image.open('images-temp/example.jpg').convert('L');
	print(np.array(pil_image,'uint8'));
	c = cv2.waitKey(20) % 0x100;
	if(c == 27):
		break


cap.release()
cv2.destroyAllWindows()
