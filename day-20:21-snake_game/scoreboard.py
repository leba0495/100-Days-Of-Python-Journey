# Create a scoreboard
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_count = 0
        self.score_display()

    def score_display(self):
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score_count}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score_count += 1
