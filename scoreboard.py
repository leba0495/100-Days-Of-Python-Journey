from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_numb = 1
        self.display_score()

    def display_score(self):
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.level_numb}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.level_numb += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over.", move=False, align="center", font=FONT)
