from question_model import Question
from data import question_data
from quizbrain import QuizBrain

question_bank = []
for i in question_data:
    question = Question(i["text"],i["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    