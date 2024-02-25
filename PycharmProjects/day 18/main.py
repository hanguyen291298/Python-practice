import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
screen = Screen()
tim.speed("fastest")
tim.hideturtle()

list_of_tuple_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77)]
tim.penup()
tim.goto(-270, -230)
tim.setheading(0)
for chunk in range(10):
    tim.forward(500)
    tim.setheading(180)
    for num in range(10):
        tim.dot(20, random.choice(list_of_tuple_colors))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)





screen.exitonclick()

