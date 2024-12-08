from flask import *

from DBManager import DBManager

app = Flask("KAHOOT")
db_name = "kahoot.db"
app.secret_key = "2503"

@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.get_quizzes()
    return render_template("index.html", quizzes=quizzes)
@app.route("/quiz/<int:quiz_id>")
def get_question(quiz_id):
    db_manager = DBManager(db_name)
    questions = db_manager.get_questions(quiz_id)
    session["questions"] = questions
    session["true_ans"] = 0
    session["quest_index"] = 0

    return redirect(url_for("show_question", quiz_id=quiz_id))

@app.route("/quiz/<int:quiz_id>/question")
def show_question(quiz_id):
    nomer = session["quest_index"]
    q = session["questions"][nomer]
    db_manager = DBManager(db_name)
    options = db_manager.get_options(q[0])

    return render_template("question.html", question=q, options=options, quiz_id=quiz_id)

@app.route("/about_school")
def about_school():
    return render_template("about_school.html")


@app.route("/quiz/<int:quiz_id>/answer",methods=["POST"])
def answer_func(quiz_id):
    session["quest_index"] += 1
    if len(session["questions"]) <= session["quest_index"]:
        return redirect(url_for("result", quiz_id=quiz_id))
    else:
        return redirect(url_for("show_question", quiz_id=quiz_id))

@app.route("/quiz/<int:quiz_id>/result")
def result(quiz_id):

    return "РЕЗУЛЬТАТ"

app.run()