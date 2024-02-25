from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -230)
        self.setheading(90)
        self.shape("turtle")
        self.shapesize(2, 2, 5)
        self.color("red")

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

    def set_position(self):
        self.goto(0, -230)

