# Import necessary libraries
from flask import Flask, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from models import MobileNet
import os
import glob
from math import floor
import copy

# Create Flask Application
app = Flask(__name__)

# Set folder location
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Instantiate mobilenet model
model = MobileNet()

# Create empty past information for the very first run of the Application
if 'img_list' not in globals():
    img_list = []
    i_ls = []
    c_ls = []

# Delete old files from the directory that are not required anymore
def manage_images(dir, img_list):
    img_list_all = glob.glob(os.path.join(dir, '*'))
    for img in img_list_all:
        if img not in img_list:
            os.remove(img)

# Create Python closures function to maintain the last processed images and predicted results
def outer():
    i = []
    p = []
    c = []
    def inner(img_pth, pred, conf):
        nonlocal i, p, c
        i.append(img_pth)
        p.append(pred)
        c.append(conf)
        if len(p) > 5:
            i.pop(0)
            p.pop(0)
            c.pop(0)
        return i, p, c
    return inner

func_add_last_5_ex = outer()

# Index or landing page
@app.route('/')
def index():
    return render_template('index.html')

# About application page
@app.route('/about')
def about():
    return render_template('about.html')

# Team info page
@app.route('/info')
def info():
    return render_template('teaminfo.html')

# Prediction result page
@app.route('/infer', methods=['POST'])
def success():
    '''
    Allows maximum three files to upload at a time.
    Calls the model to predict the classes and provide confidence score for each uploaded image
    Saves and manages the images and predicted result to show as past information in the next transaction
    '''
    if request.method == 'POST':
        ic = []
        uploaded_files = request.files.getlist("file[]")
        if len(uploaded_files) > 3:
            return '''<h1>Maximum three images allowed to upload at a time. Please go back to previous screen.</h1>'''
        global img_list, i_ls, c_ls
        img_list_o, i_ls_o, c_ls_o = copy.deepcopy(img_list), copy.deepcopy(i_ls), copy.deepcopy(c_ls)
        manage_images(app.config['UPLOAD_FOLDER'], img_list_o)
        new_images = []
        for f in uploaded_files:
            file_name = secure_filename(f.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            f.save(file_path)
            new_images.append(file_path)
            i, c = model.infer(file_path)
            # make a percentage with 2 decimal points
            c = floor(c * 10000) / 100
            ic.append((i, c))
            img_list, i_ls, c_ls = func_add_last_5_ex(file_path, i, c)

        # respond with the inference
        return render_template('inference.html', ic=ic, img_list=img_list_o, new_images=new_images,
                                i_ls=i_ls_o, c_ls=c_ls_o, last_5_idx_list=list(range(len(img_list_o))), length_list=list(range(len(new_images))))

# Fetch images from the folder to show on screen
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True) 
