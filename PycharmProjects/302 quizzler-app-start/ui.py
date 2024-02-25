import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UiInterFace:
    def __init__(self, quiz_bank):
        self.question = QuizBrain(quiz_bank)
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score: {self.question.score}", background=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some questions", fill=THEME_COLOR, font=("arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        right_pic = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_pic, highlightthickness=0, command=self.true_answer)
        self.right_button.grid(row=2, column=1)

        wrong_pic = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_pic, highlightthickness=0, command=self.false_answer)
        self.wrong_button.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.question.still_has_questions():
            self.label.config(text=f"Score: {self.question.score}")
            self.new_q = self.question.next_question()
            self.canvas.itemconfig(self.question_text, text=self.new_q)
        else:
            self.canvas.itemconfig(self.question_text, text="You finished all of the questions.")

    def true_answer(self):
        is_right = self.question.check_answer("True")
            #self.label.config(text=f"score: {self.score}")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.question.check_answer("False")
                    #self.label.config(text=f"score: {self.score}")
        self.give_feedback(is_right)

    def give_feedback(self, isright):
        if isright:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
