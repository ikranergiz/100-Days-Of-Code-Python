import smtplib
import datetime as dt
import random

MY_EMAIL = "testikra07@gmail.com"
PASSWORD = "abcdexample"
# password = "qfhnjvjugeglflrw" password of yahoo test mail -> smtp.mail.yahoo.com

now = dt.datetime.now()
weekday = now.weekday()  # 0 monday 1 tuesday

if weekday == 0:
    with open("quotes.txt") as file:
        data = file.read()
        list_of_quotes = data.split("\n")

        # all_quotes = file.readlines()
        # quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="testikra07@yahoo.com",
                            msg=f"Subject:Monday Motivation\n\n{random.choice(list_of_quotes)}.")
