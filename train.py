import os
import cv2
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__)); #directory to parents folder; 
img_dir = os.path.join(BASE_DIR,'images');

face_detect =   cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml');
face_recognizer =cv2.face.LBPHFaceRecognizer_create();

def update():
	current_id = 0;
	label_ids = {};
	y_labels = [];
	x_train = [];
	for root,dirs,files in os.walk(img_dir):
		for file in files:
			if file.endswith('png') or file.endswith('jpg') or file.endswith('jpeg'):
				path = os.path.join(root,file) # absolute path to directory content the file
				label = os.path.basename(os.path.dirname(path)); # os.path.dirname(path)==path of image directory,label is name of the image directory
				if label not in label_ids:# checking the label is in label_ids o not? add it in,
					label_ids[label] = current_id;
					print(label_ids[label],label);
					current_id += 1;
				id_ = label_ids[label];#get ids of the image
				pil_image = Image.open(path).convert('L'); #convert image to array
				size = (150,200);
				pil_image = pil_image.resize(size,Image.ANTIALIAS)
				# pil_image = cv2.imread(path,1);
				# pil_image = cv2.cvtColor(pil_image,cv2.COLOR_BGR2GRAY);
				images_array = np.array(pil_image,'uint8');# number array of a image
				faces = face_detect.detectMultiScale(images_array,scaleFactor=1.5,minNeighbors=5);#detect face in image

				for(x,y,w,h) in faces:
					roi = images_array[y:y+h,x:x+w]; #int array of face 
					x_train.append(roi);
					y_labels.append(id_);

	with open('data/label.pickle','wb') as f:
		pickle.dump(label_ids,f);

	face_recognizer.train(x_train,np.array(y_labels));
	face_recognizer.save('data/trainner.yml');
