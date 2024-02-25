import sys
from tkinter import*
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    with open(r"data\Word_to_learn.csv", encoding="utf-8") as a_file:
        data = pandas.read_csv(a_file)
except:
    with open(r"data\english_words.csv", encoding="utf-8") as a_file:
        original_file = pandas.read_csv(a_file)
        dict = original_file.to_dict(orient="records")
else:
    dict = data.to_dict(orient="records")

current_card = {}

def vietnamese_meaning(data_row):
    meaning_word = data_row["Vietnamese"]
    back_img = PhotoImage(file=r"images\card_back.png")
    canvas.itemconfig(front, image=back_img)
    canvas.itemconfig(title, text="Vietnamese", fill="white")
    canvas.itemconfig(learn_new_word, text=meaning_word, fill="white")


def random_English():
    global current_card
    if len(dict) > 0:
        current_card = random.choice(dict)
        new_word = current_card["English"]
        canvas.itemconfigure(front, image=front_img)
        canvas.itemconfigure(title, text="English", fill="black")
        canvas.itemconfigure(learn_new_word, text=new_word, fill="black")
        window.after(3000, vietnamese_meaning, current_card)
    else:
        sys.exit()

def already_known():
    try:
        dict.remove(current_card)
    except ValueError:
        sys.exit()
    else:
        new_data = pandas.DataFrame(dict)
        new_data.to_csv(r"data\Word_to_learn.csv", index=False)
        random_English()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file=r"images\card_front.png")
front = canvas.create_image(400, 263, image=front_img)
learn_new_word = canvas.create_text(400, 300, text="Word", font=("arial", 40, "bold"))
title = canvas.create_text(400, 200, text="Title", font=("arial", 35, "italic"))
canvas.grid(row=0, column=0, columnspan=3)

random_English()
wrong_img = PhotoImage(file=r"images\wrong.png")
unknown_button = Button(image=wrong_img, command=random_English)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file=r"images\right.png")
known_button = Button(image=right_img, command=already_known)
known_button.grid(row=1, column=2)
window.mainloop()
