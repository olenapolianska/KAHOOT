from flask import *

from DBManager import DBManager

app = Flask("KAHOOT")
db_name = "kahoot.db"

@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.get_quizzes()
    return render_template("index.html", quizzes=quizzes)

@app.route("/about_school")
def about_school():
    return render_template("about_school.html")


app.run()