import cv2
import getface
import getname
import adduser
import database
import train
import os
import datetime

cap = cv2.VideoCapture(0);
print('WELCOME BACK!');
print('1. Check in/out');
print('2. Add user');
print('3. Check login list');
print('------------------------------------------');
press = input();
print('---');

if(press == '1'):
	while (True):
		ret, frame = cap.read();
		faces = getface.face(frame);
		name = getname.name(frame,faces);
		cv2.imshow('frame', frame);
		if(cv2.waitKey(20) & 0xff == ord('y')):
			x = datetime.datetime.now()
			time = x.strftime('%H:%M:%S')
			if(database.checklogin(name)==0):
				print(name+' has checked in today in '+time);
			if(database.checklogin(name)==1):
				print(name+' has checked out today in '+time);
			database.checkin(name);
			break;
		c = cv2.waitKey(20) % 0x100;
		if(c == 27):
			break
if(press == '2'):
	print('PLEASE ADD SOME INFO ABOUT THIS USER');
	print('Name: ');name = input();
	print('Position: ');position = input();
	print('Phone: ');phone = input();
	print('Sex: ');sex = input();
	exist = database.add(name,position,phone,sex);
	if(exist is True):
		path = r'images/'+name;
		os.makedirs(path);
		while(True):
			ret,frame = cap.read();
			adduser.add(path,frame);
			c = cv2.waitKey(20) % 0x100
			if(c == 27):
				break
		train.update();
		print(name+'has been added')
	if(exist is False):
		print(name+' has been existed');
if(press == '3'):
	print('1. Today');
	print('2. Another day');
	print('------------------------------------------');
	day = input();
	print('---');
	if(day == '1'):
		database.attendance('now');
	if(day == '2'):
		print('Enter a day:')
		print('------------');
		day = input()
		print('------------');
		database.attendance(day);
cap.release()
cv2.destroyAllWindows()

