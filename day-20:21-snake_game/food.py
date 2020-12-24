from turtle import Turtle
import random


class Food(Turtle):
    """To display the food, we need to create a Food class. This class will inherit all the attributes from turtle
    class. Then we can manipulate the attributes inherited from turtle as needed to create the food that the snake
    will eat. """

    def __init__(self):
        # Syntax needed for inheritance
        super().__init__()
        self.shape("circle")
        self.penup()
        # Since we want a smaller circle than the standard size, we use the shapesize method to shrink the
        # circle by half.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    # Detect collision with food
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
