import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import keras
from keras.models import load_model
import tensorflow as tf
from keras.optimizers import RMSprop
from keras import backend as K
from os import listdir
from os.path import isfile, join
import re

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			image = cv2.imread(os.path.dirname(os.path.realpath(__file__))+"/uploads/"+filename)
			color_result = getDominantColor(image)
			detection = detect(image)
			return jsonify({"MainColor": color_result, "Item": detection} )
	return '''
	<!doctype html>
	<title>API</title>
	<h1>API Running Successfully</h1>'''

def detect(image):
	model = load_model('recycle2.h5')	
	image = cv2.resize(image, (100,100), interpolation = cv2.INTER_AREA)
	image = image.reshape(1,100,100,3) 
	classes = model.predict(image, batch_size = 1)
	print(str(classes))
	final = np.argmax(classes,axis=-1)
	arr = ["Cardboard","Glass","Metal", "Paper", "Plastic", "Trash" ]
	a = arr[final[0]]
	res = str(a)
	K.clear_session()
	return res

def getDominantColor(image):
	'''returns the dominant color among Blue, Green and Reds in the image '''
	B, G, R = cv2.split(image)
	B, G, R = np.sum(B), np.sum(G), np.sum(R)
	color_sums = [B,G,R]
	color_values = {"0": "Blue", "1":"Green", "2": "Red"}
	return color_values[str(np.argmax(color_sums))]


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
