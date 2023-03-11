from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/uploads"
app.config['SECRET_KEY'] = 'aufjshrugeioshnu'

# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#     username="colorfulcounseli",
#     password="WinnerGirls!",
#     hostname="colorfulcounseling.mysql.pythonanywhere-services.com",
#     databasename="colorfulcounseli$journals",
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)
# import models

your_own_prompt = "Or, use your own prompt"
with app.open_resource('static/sculpt_prompts.txt') as f:
    contents = f.read().decode("utf-8")
    sculpt_prompts = contents.split('\n') + [your_own_prompt]
with app.open_resource('static/draw_prompts.txt') as f:
    contents = f.read().decode("utf-8")
    draw_prompts = contents.split('\n') + [your_own_prompt]
with app.open_resource('static/photography_prompts.txt') as f:
    contents = f.read().decode("utf-8")
    photography_prompts = contents.split('\n') + [your_own_prompt]
with app.open_resource('static/collage_prompts.txt') as f:
    contents = f.read().decode("utf-8")
    collage_prompts = contents.split('\n') + [your_own_prompt]

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

@app.route("/journals/new")
def new():
    return render_template('new.html')

@app.route("/journals/photography", methods=["GET", "POST"])
def photography():
    if request.method == "POST":
        file = request.files['file']
        if request.form['prompt'] == your_own_prompt:
            prompt = request.form['custom-prompt']
        else:
            prompt = request.form['prompt']
        session['prompt'] = prompt
        title = request.form['title']
        session['title'] = title
        if file:
            filename = secure_filename(file.filename)
            session['image'] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('write'))

    return render_template('photography.html', prompts = photography_prompts)

@app.route("/journals/collage", methods=["GET", "POST"])
def collage():
    if request.method == "POST":
        file = request.files['file']
        if request.form['prompt'] == your_own_prompt:
            prompt = request.form['custom-prompt']
        else:
            prompt = request.form['prompt']
        session['prompt'] = prompt
        title = request.form['title']
        session['title'] = title
        if file:
            filename = secure_filename(file.filename)
            session['image'] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('write'))

    return render_template('collage.html', prompts = collage_prompts)

@app.route("/journals/draw", methods=["GET", "POST"])
def draw():
    if request.method == "POST":
        file = request.files['file']
        if request.form['prompt'] == your_own_prompt:
            prompt = request.form['custom-prompt']
        else:
            prompt = request.form['prompt']
        session['prompt'] = prompt
        title = request.form['title']
        session['title'] = title
        if file:
            filename = secure_filename(file.filename)
            session['image'] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('write'))
        else:
            print("no file")

    return render_template('draw.html', prompts = draw_prompts)

@app.route("/journals/sculpt", methods=["GET", "POST"])
def sculpt():
    if request.method == "POST":
        file = request.files['file']
        if request.form['prompt'] == your_own_prompt:
            prompt = request.form['custom-prompt']
        else:
            prompt = request.form['prompt']
        session['prompt'] = prompt
        title = request.form['title']
        session['title'] = title
        if file:
            filename = secure_filename(file.filename)
            session['image'] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('write'))

    return render_template('sculpt.html', prompts = sculpt_prompts)

@app.route("/journals/write", methods=["GET", "POST"])
def write():
    if request.method == "POST":
        entry1 = request.form['prompt1']
        entry2 = request.form['prompt2']
        entry3 = request.form['prompt3']
        mood = request.form['mood']

        journal = models.Journal(prompt=session['prompt'], title=session['title'], image=session['image'], entry1=entry1, entry2=entry2, entry3=entry3, mood=mood)
        db.session.add(journal)
        db.session.commit()

        session['prompt'] = ''
        session['title'] = ''
        session['image'] = ''

        return redirect(url_for('journals'))

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
    conn = sqlite3.connect('mood_tracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO mood_data (month, day, mood) VALUES (?, ?, ?)", (month, day, mood))
    conn.commit()
    conn.close()

    return ""
