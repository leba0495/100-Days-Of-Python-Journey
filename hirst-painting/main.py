# import colorgram
# def get_tuple(color_numbers):
#     return tuple(list(color_numbers))
#
#
# color = colorgram.extract('image.jpg', 20)
# for c in range(20):
#     colors = color[c]
#     rgb = colors.rgb
#     color_list.append(get_tuple(rgb))
# print(color_list)

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122),
              (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202),
              (232, 221, 225), (58, 47, 41)]


def random_color(rgb_list):
    return random.choice(rgb_list)


def reposition_turtle():
    tim.penup()
    tim.setposition(-300, -300)


reposition_turtle()
y = -300
numb_of_dots = 0
while numb_of_dots < 100:
    for _ in range(10):
        tim.dot(20, random_color(color_list))
        tim.fd(50)
        y += 5
        numb_of_dots += 1
    tim.setposition(-300, y)
screen.exitonclick()
