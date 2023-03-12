from click import prompt
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy
import urllib
import time
from app.promptGenarator import chatbot, generateQuestionsPhoto, generateQuestionsDrawing
from app.image_recognition import guess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/uploads"
app.config['SECRET_KEY'] = 'aufjshrugeioshnu'

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="colourfulcounsel",
    password="pinkmonster",
    hostname="colourfulcounseling.mysql.pythonanywhere-services.com",
    databasename="colourfulcounsel$journals",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# from app import models

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

@app.route("/journal/<id>")
def journal(id):
    journal = db.session.query(models.Journal).get(id)
    return render_template("journal.html",journal=journal)

@app.route("/journals")
def journals():
    journals = db.session.query(models.Journal).all()
    return render_template('journals.html', journals=journals)

@app.route("/journals/draw-prompt", methods=["GET", "POST"])
def draw_prompt():
    if request.method == "POST":
        reply = chatbot("Generate a drawing prompt. Do not include any follow-up questions.")
    else:
        reply = chatbot("Generate a drawing prompt. Do not include any follow-up questions.")
    session["prompt"] = reply
    return render_template("draw_prompt.html", prompt=reply)

@app.route("/journals/photo-prompt", methods=["GET", "POST"])
def photo_prompt():
    if request.method == "POST":
        reply= chatbot("Generate a prompt about taking photos for art therapy. Do not include any follow-up questions.")
    else:
        reply= chatbot("Generate a prompt about taking photos for art therapy. Do not include any follow-up questions.")
    session["prompt"] = reply
    return render_template("photo_prompt.html", photoprompt=reply)

@app.route("/journals/draw", methods=["GET", "POST"])
def draw():
    if request.method == "POST":
        title = request.form['title']
        session['title'] = title
        description = request.form['description']
        questions = generateQuestionsDrawing(session['prompt'],description)
        session['questions'] = questions
        return redirect(url_for('write'))
    
    return render_template('draw.html', prompt = session['prompt'])

@app.route("/journals/draw/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        questions = generateQuestionsDrawing(session['prompt'],description)
        session['questions'] = questions
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            session['image'] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('write'))
        
    return render_template('upload.html', prompt = session['prompt'])

@app.route('/journals/photo', methods = ['GET', 'POST'])
def photo():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            session['image'] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            about = guess("static/uploads/"+filename)
            questions = generateQuestionsPhoto(session['prompt'],about)
            session['questions'] = questions
            return redirect(url_for('write')) 
        
    return render_template('photo.html', prompt = session['prompt'])

@app.route("/journals/write", methods=["GET", "POST"])
def write():
    if request.method == "POST":
        entry1 = request.form['prompt1']
        entry2 = request.form['prompt2']
        entry3 = request.form['prompt3']
        mood = request.form['mood']

        journal = models.Journal(prompt=session['prompt'], 
                                 title=session['title'], 
                                 image=session['image'], 
                                 questions=session['questions'],
                                 entries=(entry1,entry2,entry3),
                                 mood=mood)
        db.session.add(journal)
        db.session.commit()

        session['prompt'] = ''
        session['title'] = ''
        session['image'] = ''

        return redirect(url_for('journals'))

    return render_template('write.html', image="uploads/"+session['image'], questions=session['questions'])

@app.route("/tutorial")
def tutorial():
    return render_template('tutorial.html')

@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/moodtracker")
def moodtracker():
    return render_template('moodtracker.html')

@app.route("/updatedfeatures")
def updatedfeatures():
    return render_template('updatedfeatures.html')

@app.route("/")
def index():
    return render_template_string(open('index.html').read())

@app.route("/submit_mood", methods=["POST"])
def submit_mood():
    month = int(request.form["month"])
    day = int(request.form["day"])
    mood = int(request.form["mood"])

    # Insert the mood data into the database
    mood = models.Mood(month = month, day = day, mood = mood)
    db.session.add(mood)
    db.session.commit()

    return ""

@app.route('/save_image', methods=['POST'])
def save_image():
    imgData = request.form['imgBase64']
    # convert to an image file
    with urllib.request.urlopen(imgData) as response:
        data = response.read()
    # save the file, filename is the current time
    now = time.strftime("%Y%m%d-%H%M%S")
    with open("static/uploads/%s.png" % now, "wb") as fh:
        fh.write(data)
    session['image'] = "%s.png" % now
    return 'success'