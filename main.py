from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    new_question = Question(text=question_text,answer=question_answer)
    question_bank.append(new_question)

#question_bank#LIST OF OBJECT WHICH CONTAIN TEEXT AND ASNWER
quiz = Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've Compleeted the quiz")
print(f"Your final score is:{quiz.score}/{quiz.question_number}")
