from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h",
               "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    random_password = []
    random_letter = [choice(letters) for letter in range(4)]
    random_symbol = [choice(symbols) for symbol in range(2)]
    random_number = [choice(numbers) for num in range(4)]
    random_password = random_number + random_letter + random_symbol
    shuffle(random_password)
    password_generate = "".join(random_password)
    password_entry.insert(0, password_generate)
    pyperclip.copy(password_generate)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_inform():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
         "Email": email,
         "Password": password
         },
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You need to fill in the information. Not allowed to be empty!")
    else:
        is_ok = messagebox.askokcancel(title="Your information", message=f"These are the detail of you information:\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as new_file:
                    json.dump(data, new_file, indent=4)
            finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)


def search_information():
    website = web_entry.get()
    try:
        with open("data.json", "r") as a_file:
            data = json.load(a_file)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "You have not had a data yet. Please fill in!")
    else:
        if website not in data:
            messagebox.showwarning("Warning", "Your file is not found")
        else:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(f"Your information of {website}", f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP----------------------------- #


window = Tk()
window.title("Generate password")
window.config(padx=100, pady=100)
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=2)


canvas = Canvas(width=200, height=200)
image_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=1, sticky="w")

web_label = Label(text="Website:")
web_label.grid(row=1, column=0, sticky="w")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="w")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, sticky="w" )
email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w" )
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1, sticky="w")

search_button = Button(text="Search", command=search_information)
search_button.grid(row=1, column=1, sticky="e")
generate_button = Button(text="Generate password", command=generate)
generate_button.grid(row=3, column=1, sticky="e")
add_button = Button(text="Add", width=35, command=save_inform)
add_button.grid(row=4, column=1)

window.mainloop()
