from flask import *

from DBManager import DBManager

app = Flask("KAHOOT")
db_name = "kahoot.db"

@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.get_quizzes()
    return render_template("index.html", quizzes=quizzes)
@app.route("/quiz1")
def quiz1():
    db_manager = DBManager(db_name)
    questions = db_manager.get_questions(4)
    options = db_manager.get_options()
    return render_template("quiz1.html", questions=questions, options=options)

@app.route("/about_school")
def about_school():
    return render_template("about_school.html")


app.run()