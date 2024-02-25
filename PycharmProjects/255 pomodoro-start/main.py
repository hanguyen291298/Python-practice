from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    label_done.config(text="")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = ""
        for i in range(math.floor(reps/2)):
            check += "✓"
            label_done.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=100, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

label_done = Label(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
label_done.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(102, 112, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()
