import turtle
from turtle import Turtle
import random

turtle.colormode(255)


class Car:
    def __init__(self):
        self.list_cars = []

    def create_car(self):
        car = Turtle()
        car.penup()
        y_positions = [i for i in range(-150, 210, 50)]
        car.goto(550, random.choice(y_positions))
        car.shape("square")
        car.shapesize(stretch_wid=1.5, stretch_len=random.randint(2, 4))
        car.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        car.setheading(180)
        self.list_cars.append(car)

    def move_car(self):
        for car in self.list_cars:
            car.forward(40)

