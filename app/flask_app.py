from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/uploads"
app.config['SECRET_KEY'] = 'aufjshrugeioshnu'

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="colorfulcounseli",
    password="WinnerGirls!",
    hostname="colorfulcounseling.mysql.pythonanywhere-services.com",
    databasename="colorfulcounseli$journals",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
import models

with app.open_resource('static/upload_prompts.txt') as f:
    contents = f.read().decode("utf-8")
    upload_prompts = contents.split('\n')
with app.open_resource('static/draw_prompts.txt') as f:
    contents = f.read().decode("utf-8")
    draw_prompts = contents.split('\n')
with app.open_resource('static/photograph_prompts.txt') as f:
    contents = f.read().decode("utf-8")
    photograph_prompts = contents.split('\n')
with app.open_resource('static/collage_prompts.txt') as f:
    contents = f.read().decode("utf-8")
    collage_prompts = contents.split('\n')
    
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

    return render_template('photography.html', prompts = photography_prompts)

@app.route("/journals/collage", methods=["GET", "POST"])
def collage():
    if request.method == "POST":
        pass

    return render_template('collage.html', prompts = collage_prompts)

@app.route("/journals/draw", methods=["GET", "POST"])
def draw():
    if request.method == "POST":
        pass

    return render_template('draw.html', prompts = draw_prompts)

@app.route("/journals/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            session['image'] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('write'))

    return render_template('upload.html', prompts = upload_prompts)

@app.route("/journals/write")
def write():
    if request.method == "POST":
        pass

    image_path = "uploads/" + session['image']
    return render_template('write.html', image=image_path)

@app.route("/tutorial")
def tutorial():
    return render_template('tutorial.html')

@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
