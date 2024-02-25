from turtle import Turtle
import highest_score
ALIGNMENT = 'center'
FONT = "arial", 13, "normal"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score} Highest score: {highest_score.HIGHEST_SCORE}", align="center", font=("Arial", 10, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} Highest score: {highest_score.HIGHEST_SCORE}", align="center", font=("Arial", 10, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 15, "bold"))

