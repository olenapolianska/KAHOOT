from DBManager import DBManager

db_manager = DBManager("KAHOOT.db")
#db_manager.create_tables()
#db_manager.add_quiz(4, "Квіз про Україну", "деякий опис")
#db_manager.add_question(1, 4, "Скільки областей в Україні?")
#print(db_manager.get_quizzes())
print(db_manager.get_questions())