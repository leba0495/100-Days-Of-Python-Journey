class QuizBrain:
    def __init__(self, q_list):
        """Models the questions that are stored in the list"""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        """Return true if there are still questions in the list"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Gets the next question after user's answer, updates the current question number"""
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False)?: ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        """Check whether user's answer is correct, updates score, and gives feedback to user"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")
