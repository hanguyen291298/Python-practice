import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import ScoreBoard
sleep_time = 0.3
screen = Screen()
screen.setup(width=1000, height=500)
screen.bgcolor("grey")
screen.title("Crossing Game")
screen.tracer(0)

player = Player()
new_car = Car()
score = ScoreBoard()

screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")
screen.onkeypress(fun=player.move_down, key="Down")
is_on = True
while is_on:
    time.sleep(sleep_time)
    screen.update()
    new_car.create_car()
    new_car.move_car()
    for c in new_car.list_cars:
        if player.distance(c) < 28:
            score.game_over()
            is_on = False
        elif player.ycor() > 280:
            score.increase_score()
            player.set_position()
            sleep_time += 0.001




















screen.exitonclick()
