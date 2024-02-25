import random
from turtle import Turtle, Screen
is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(prompt="What color do you choose?", title="Bet")

colors = ["red", "green", "yellow", "black", "blue", "purple"]
ycor = -320
turtles = []
for i in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(-450, ycor)
    ycor += 100
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        if turtle.xcor() > 450:
            is_race_on = False
            turtle_win = turtle.pencolor()
            if turtle_win == user_bet:
                print(f"you win. The {turtle_win} turtle is winner")
            else:
                print(f"You lose. The {turtle_win} turtle is winner")
            is_race_on = False
        else:
            turtle.forward(random_distance)


screen.exitonclick()