import datetime as dt
import random
import smtplib

my_email = "han655442@gmail.com"
password = "vdhsurrbndizorji"



current_day = dt.datetime.now()
week_day = current_day.weekday()

#if week_day == 0:
with open("quotes.txt") as file:
    list_of_quotes = file.readlines()
    random_sentence = random.choice(list_of_quotes).split("-")
    quote = random_sentence[0]
    authur = random_sentence[1]

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="thuyha291298@gmail.com", msg=f"Subject: Nice words of every morning\n\n{quote}\n{authur}")


