from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from werkzeug.utils import secure_filename
from models import MobileNet
import os
import glob
from math import floor
import base64
import io
from collections import namedtuple

app = Flask(__name__)

# app.config['UPLOAD_FOLDER'] = 'uploads'
UPLOAD_FOLDER = 'uploads' # path_change
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = MobileNet()

def manage_images(dir, lim):
    img_list = glob.glob(os.path.join(dir, '*'))
    keep_list = img_list[lim*-1:]
    for img in img_list:
        if img not in keep_list:
            os.remove(img)
    return keep_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/info')
def info():
    return render_template('teaminfo.html')

@app.route('/infer', methods=['POST'])
def success():
    if request.method == 'POST':
        ic = []
        # f = request.files['file']
        uploaded_files = request.files.getlist("file[]")
        if len(uploaded_files) > 3:
            return '''<h1>Only three images allowed to upload at a time</h1>'''
        img_list = manage_images(app.config['UPLOAD_FOLDER'], 5)
        new_images = []
        for f in uploaded_files:
            file_name = secure_filename(f.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            # f.save(saveLocation)
            f.save(file_path)
            new_images.append(file_path)
            image_url = url_for('uploaded_file', filename=file_name)
            # i, c = model.infer(saveLocation)
            i, c = model.infer(file_path)
            # make a percentage with 2 decimal points
            c = floor(c * 10000) / 100
            # delete file after making an inference
            # os.remove(saveLocation)
            # inference.append(i)
            # confidence.append(c)
            ic.append((i, c))
        # respond with the inference
        
        return render_template('inference.html', ic=ic, img_list=img_list, new_images=new_images, length_list=list(range(len(new_images))))
        # return render_template('inference.html', name=inference, confidence=confidence)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True) 
