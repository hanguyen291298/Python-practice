import turtle
from turtle import Screen
import pandas

screen = Screen()
screen.title("US_States_game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

correct_answer = 0

data = pandas.read_csv("50_states.csv")
list_states = data["state"].to_list()
guessed_list = []

while correct_answer < 50:
    your_answer = turtle.textinput(f"{correct_answer}/50 states correct", "What is the next state?").title()
    if your_answer == "Exit":
        state_learn = [st for st in list_states if st not in guessed_list]
        new_data = pandas.DataFrame(state_learn)
        new_data.to_csv("state_to_learn.csv")
        break
    if your_answer in list_states:
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        x_cor = data[data["state"] == your_answer].x
        y_cor = data[data["state"] == your_answer].y
        tim.goto(int(x_cor), int(y_cor))
        tim.write(f"{your_answer}")
        correct_answer += 1
        guessed_list.append(your_answer)


screen.mainloop()
