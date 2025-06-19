from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for text in question_data:
    question = Question(text["question"], text["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.questions()
    print(f"Your current score is {quiz.score}/{quiz.question_number}\n")

print("Congratulations! you've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
