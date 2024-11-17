from flask import *

app = Flask("KAHOOT")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_school")
def about_school():
    return render_template("about_school.html")


app.run()