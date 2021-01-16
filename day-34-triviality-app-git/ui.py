from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterFace:

    def __init__(self, quiz_brain: QuizBrain):
        """To model the GUI and allow a more visual appealing experience"""
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Triviality")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="There will be a question here.",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(pady=50, column=0, row=1, columnspan=2)

        self.score = Label(padx=20, pady=20, text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        check_mark_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=check_mark_img, highlightthickness=0, command=self.true_check)
        self.true_button.grid(column=0, row=2)

        x_mark_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=x_mark_img, highlightthickness=0, command=self.false_check)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've answered all the question in the trivia.")
            # Buttons need to be disabled because once the questions have been answered it would allow the user to keep
            # to keep changing the screen
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check(self):
        self.provide_feedback(self.quiz.check_answer("True"))

    def false_check(self):
        self.provide_feedback(self.quiz.check_answer("False"))

    def provide_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
