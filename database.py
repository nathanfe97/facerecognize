import mysql.connector
import os
import cv2
import time
db = mysql.connector.connect(host='localhost',user='root',passwd='ROOT',db='facerecog');
cur = db.cursor();


def checkin(name):
	login = checklogin(name);
	if (name is not '') & (login == 0):
		sql = 'insert into attendance(name,dateoftime,timelogin,timelogout) values("'+name+'",now(),now(),"00:00:00")';
		cur.execute(sql);
	elif (name is not '') & (login == 1 ):
		sql = "update attendance set timelogout=now() where name ='"+name+"' && dateoftime =date(now())";
		cur.execute(sql);
	db.commit();

def checklogin(name):
	sql='select name from attendance where dateoftime=date(now())';
	login = 0;
	cur.execute(sql);
	for x in cur:
		if name in x[0]:
			login=1;
	# timelogin= str(timelogin);
	return login;

def add(name,position,phone,sex):
	checksql = 'select * from employer where name="'+name+'";'
	cur.execute(checksql);
	emp = '';
	for x in cur:
		emp = x[0];
	# emp = str(emp);
	if(emp is ''):
		sql = 'insert into employer values("'+name+'","'+position+'","'+phone+'","'+sex+'");'
		cur.execute(sql);
		db.commit();
		return True;
	else:
		return False;

def attendance(dateoftime):
	if(dateoftime == 'now'):
		sql ='select * from attendance where dateoftime=date(now());';
	else:
		sql ='select * from attendance where dateoftime="'+dateoftime+'";';
	cur.execute(sql);
	i=0;
	for x in cur:
		i=i+1;
		if(x[3] is not '00:00:00'):
			print(str(i),'- ',x[0],'| login: ',str(x[2]),' | logout: ',str(x[3]));

