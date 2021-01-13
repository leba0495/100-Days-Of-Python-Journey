import smtplib
import datetime as dt
import pandas
import random

birthday_file = pandas.read_csv("birthdays.csv")

the_day_of = dt.datetime.now()
the_day_of_birthday = (the_day_of.month, the_day_of.day)

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_file.iterrows()}
letter_numb = random.randint(1, 3)

my_email = "lifevicebyluis@gmail.com"
my_password = "Brito_LV_arias25"

if the_day_of_birthday in birthdays_dict:
    birthday_person = birthdays_dict[the_day_of_birthday]
    with open(f"./letter_templates/letter_{letter_numb}.txt", mode="r") as rand_letter:
        chosen_letter = rand_letter.read()
        chosen_letter = chosen_letter.replace("[NAME]", birthday_person['name'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject: Birthday Wishes!\n\n{chosen_letter}"
        )
