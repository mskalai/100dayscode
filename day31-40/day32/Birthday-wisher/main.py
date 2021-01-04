import smtplib
import pandas
import datetime
import random

#myinfo
mymail="msdtesting07@gmail.com"
password="abcdef(123)"

#mail sending
def mail(mail,msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mymail,password=password)
        connection.sendmail(
            from_addr=mymail,
            to_addrs=mail,
            msg=f"Subject:Happy Birthday!\n{msg}"
        )

#file reading
file=pandas.read_csv("birthdays.csv")
bday=pandas.DataFrame(file)
bday_list=bday.to_dict(orient='records')

with open("letter_templates/letter_1.txt") as let1:
    mdl1=let1.read()
with open("letter_templates/letter_2.txt") as let2:
    mdl2=let2.read()
with open("letter_templates/letter_3.txt") as let3:
    mdl3 =let3.read()
let_mdl=[mdl1,mdl2,mdl3]
mdl=random.choice(let_mdl)

#date&time
dt=datetime.datetime.now()
cur_year=dt.year
cur_month=dt.month
cur_day=dt.day

for i in bday_list:
    if(i["month"]==cur_month and i["day"]==cur_day):
        mail(mail=i["email"],msg=mdl.replace("[NAME]",i["name"]))






