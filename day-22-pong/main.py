from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong: The Famous Arcade Game")
screen.setup(width=800, height=600)

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect ball collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()
    # Detect when l_paddle misses
    if ball.xcor() < -390:
        ball.reset_ball()
        score.r_point()


screen.exitonclick()
