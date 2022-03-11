from datetime import date, datetime

user_input = str(input('Enter date(yyyy-mm-dd): '))
user_birthday = datetime.strptime(user_input, "%Y-%m-%d").date()
today = date.today()
time_difference = today - user_birthday
D = time_difference.days
M = int(D/365)*12
Y = int(D/365)

print(f'Age is : {Y} year , {M} Month , {D} Days')
