class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's the correct answer.")
            self.score += 1
        else:
            print(f"That's the wrong answer. The correct answer is {correct_answer}")

    def questions(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} {current_question.text} (True/False)? ").lower()
        self.check_answer(user_answer, current_question.answer)