from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize()
window.config(padx=20, pady=20)


def calculate():
    mile = mile_input.get()
    km = float(mile) * 1.609
    label_output.config(text=km)

label_1 = Label(text="equal to", font=("Arial", 20, "bold"))
label_1.grid(row=1, column=0)
label_2 = Label(text="Miles", font=("Arial", 20, "bold"))
label_2.grid(row=0, column=2)
label_3 = Label(text="Km", font=("Arial", 20, "bold"))
label_3.grid(row=1, column=2)

mile_input = Entry(width=10)
mile_input.insert(END, "0")
mile_input.grid(row=0, column=1)
label_output = Label(text="0")
label_output.grid(row=1, column=1)


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)




window.mainloop()