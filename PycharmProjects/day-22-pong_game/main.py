from turtle import Screen
from paddle import CreatePaddle
from ball import Ball
import time
from scoreboard import ScoreBoard

import os
print(os.getcwd())
screen = Screen()

screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = CreatePaddle(-380, 0)
r_paddle = CreatePaddle(380, 0)

ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and r_paddle.xcor() > 350 or ball.distance(l_paddle) < 50 and l_paddle.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.set_position()
        score.increase_l_score()

    elif ball.xcor() < -400:
        ball.set_position()
        score.increase_r_score()


screen.exitonclick()
