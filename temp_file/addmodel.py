import cv2
import os
import numpy as np
import time

cap = cv2.VideoCapture(0);

namedir = input('Name of model: ');
path = r'images/'+namedir;

if not os.path.exists(path):
	os.makedirs(path);
while True:
	shot = 0;
	number = 1;
	ret, frame = cap.read();

	filename = str(time.time())+'.jpg';
	filepath = os.path.join(path,filename);

	x = 180; w = 300;
	y = 40; h = 400;

	roi_frame = frame[y:y+h,x:x+w];

	
	text1 = 'Please put your face here';
	text2 = 'S to shot, Z to end';
	cv2.putText(frame,text1,(x-30,y-15),cv2.FONT_HERSHEY_SIMPLEX,1,(250,0,0),2,cv2.LINE_AA); 
	cv2.rectangle(frame,(x,y),(x+w,y+h),(0, 50, 150),5);
	cv2.putText(frame,text2,(x+10,y+h+30),cv2.FONT_HERSHEY_SIMPLEX,1,(250,0,0),2,cv2.LINE_AA); 
	cv2.imshow('webcam',frame);

	if cv2.waitKey(2) & 0xFF == ord('s'):
		shot = 1;

	if (shot != 0):
		cv2.imwrite(filepath,roi_frame);
		# shot = 0;

	if cv2.waitKey(1) & 0xFF == ord('z'):
		break
	
cap.release();
cv2.destroyAllWindows();
	
