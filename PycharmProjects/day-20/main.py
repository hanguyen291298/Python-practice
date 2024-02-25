from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import highest_score
import random
import time


def play_game():
    sleep_time = 0.5
    screen = Screen()
    screen.listen()
    screen.tracer(0)
    screen.bgcolor("black")
    screen.setup(width=400, height=400)
    screen.title("My_snake_game")

    segment = Snake()
    food = Food()
    score = ScoreBoard()

    screen.onkey(fun=segment.move_left, key="Left")
    screen.onkey(fun=segment.move_right, key="Right")
    screen.onkey(fun=segment.move_up, key="Up")
    screen.onkey(fun=segment.move_down, key="Down")

    is_game_on = True
    while is_game_on:
        time.sleep(sleep_time)
        screen.update()
        segment.move()
        for seg in segment.snakes_list:
            if food.distance(seg) < 15:
                segment.add_segment()
                food.goto(random.randint(-180, 180), random.randint(-180, 180))
                score.increase_score()
            elif seg.xcor() > 190:
                segment.snakes_list[0].goto(-190, seg.ycor())
            elif seg.xcor() < -190:
                segment.snakes_list[0].goto(190, seg.ycor())
            elif seg.ycor() > 190:
                segment.snakes_list[0].goto(seg.xcor(), -190)
            elif seg.ycor() < -190:
                segment.snakes_list[0].goto(seg.xcor(), 190)
            elif seg != segment.snakes_list[0]:
                if segment.snakes_list[0].distance(seg) < 15:
                    score.game_over()
                    if score.score > highest_score.HIGHEST_SCORE:
                        highest_score.HIGHEST_SCORE = score.score
                        with open("highest_score.py", "w") as file:
                            file.write(f"HIGHEST_SCORE = {highest_score.HIGHEST_SCORE}")
                    ask_user = screen.textinput(prompt="Do you want to continue? y or n", title="Play game").lower()
                    if ask_user == "y":
                        screen.clear()
                        play_game()
                    else:
                        is_game_on = False

    screen.exitonclick()


play_game()











