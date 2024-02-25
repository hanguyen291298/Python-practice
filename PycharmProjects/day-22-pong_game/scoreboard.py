from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.l_score = 0
        self.r_score = 0
        self.write(f"Score: {self.l_score} | {self.r_score}", align="center", font=("Arial", 20, "bold"))

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"Score: {self.l_score} | {self.r_score}", align="center", font=("Arial", 20, "bold"))

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"Score: {self.l_score} | {self.r_score}", align="center", font=("Arial", 20, "bold"))

