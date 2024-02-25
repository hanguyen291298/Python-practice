from datetime import datetime
import pandas
import random
import smtplib
my_email = "han655442@gmail.com"
my_password = "vdhsurrbndizorji"

current_time = datetime.now()
Month = current_time.month
Date = current_time.day
NAME = "[NAME]"
with open("birthdays.csv") as file:
    data = pandas.read_csv(file, index_col=None)
    for (index, row) in data.iterrows():
        if row.month == Month and row.day == Date:
            name = row["name"]
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            email_to_send = row.email
            random_letter = f"letter_templates\letter_{random.randint(1, 3)}.txt"
            with open(random_letter) as a_file:
                letter_data = a_file.readlines()
                message = """"""
                for line in letter_data:
                    new_line = line.replace(NAME, name)
                    message += new_line

                connection.sendmail(from_addr=my_email, to_addrs=email_to_send, msg=f"Subject: Wish you a nice day\n\n{message}")



