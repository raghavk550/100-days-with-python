import smtplib, datetime as dt, random, pandas
from turtledemo.clock import current_day

my_email = "abc@gmail.com"
password = "nctewajhlmdnfyjb"

# with open("quotes.txt") as file:
#     quotes = file.read().splitlines()
#
# current_day = dt.datetime.now().weekday()
#
# if current_day == 4:
#     connection = smtplib.SMTP('smtp.gmail.com')
#     connection.starttls()  # to secure email TLS - Transport Layer Security
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="rkrk@yopmail.com",
#                         msg=f"Subject: Hello World!\n\n{random.choice(quotes)}")
#     connection.close()

data_frame = pandas.read_csv("./birthdays.csv")
birthdays_arr = data_frame.to_dict(orient="records")
current_date_time = dt.datetime.now()
current_month = current_date_time.month
current_date = current_date_time.day
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for birthday in birthdays_arr:
    if birthday["month"] == current_month and birthday["day"] == current_date:
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()  # to secure email TLS - Transport Layer Security
        connection.login(user=my_email, password=password)
        with open(random.choice(letters)) as file:
            content = file.read()
            content = content.replace("[NAME]", birthday["name"])
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday["email"],
                                msg=f"Subject: Happy Birthday!\n\n{content}")
        connection.close()


