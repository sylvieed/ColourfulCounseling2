from flask import Flask, render_template, request

app = Flask(__name__)

print("HELLO")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/info")
def info():
    return render_template('info.html')

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

@app.route("/journals/upload")
def upload():
    if request.method == "POST":
        pass

    return render_template('upload.html')

@app.route("/journals/write")
def write():
    if request.method == "POST":
        pass

    return render_template('write.html')
