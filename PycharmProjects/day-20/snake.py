from turtle import Turtle
X_Y = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class Snake:
    def __init__(self):
        self.snakes_list = []
        self.create_snake()

    def create_snake(self):
        for position in X_Y:
            segment = Turtle("circle")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.snakes_list.append(segment)

    def add_segment(self):
        new_segment = Turtle("circle")
        new_segment.penup()
        new_segment.color("white")
        x_position = self.snakes_list[-1].xcor() - 20
        y_position = self.snakes_list[-1].ycor()
        new_segment.goto(x_position, y_position)
        self.snakes_list.append(new_segment)

    def move(self):
        for seg in range(len(self.snakes_list) - 1, 0, -1):
            new_xcor = self.snakes_list[seg - 1].xcor()
            new_ycor = self.snakes_list[seg - 1].ycor()
            self.snakes_list[seg].goto(new_xcor, new_ycor)
        self.snakes_list[0].forward(DISTANCE)

    def move_left(self):
        if self.snakes_list[0].heading() != 0:
            self.snakes_list[0].setheading(180)

    def move_right(self):
        if self.snakes_list[0].heading() != 180:
            self.snakes_list[0].setheading(0)

    def move_up(self):
        if self.snakes_list[0].heading() != 270:
            self.snakes_list[0].setheading(90)

    def move_down(self):
        if self.snakes_list[0].heading() != 90:
            self.snakes_list[0].setheading(270)




