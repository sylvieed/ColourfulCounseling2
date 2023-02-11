from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads/"

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

@app.route("/journals")
def journals():
    return render_template('journals.html')

@app.route("/journals/new")
def new():
    return render_template('new.html')

@app.route("/journals/photography", methods=["GET", "POST"])
def photography():
    if request.method == "POST":
        pass

    return render_template('photography.html')

@app.route("/journals/collage", methods=["GET", "POST"])
def collage():
    if request.method == "POST":
        pass

    return render_template('collage.html')

@app.route("/journals/draw", methods=["GET", "POST"])
def draw():
    if request.method == "POST":
        pass

    return render_template('draw.html')

@app.route("/journals/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('journals'))

    return render_template('upload.html')

@app.route("/journals/write")
def write():
    if request.method == "POST":
        pass

    return render_template('write.html')
