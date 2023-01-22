
from datetime import datetime as dt
import datetime
# Implement a function that receives a float number that represents
# the amount of seconds as argument, and returns a formatted string that displays
# the amount of seconds in the format: hh:mm:ss.
# Hint: use datetime.timedelta for one-liner code
#

val = float(input("insert seconds "))
def watch():
    ret_val = datetime.timedelta(seconds=val)
    return str(ret_val)

print(watch())


# Implement a function that gets a string that represents datetime in the
# following format: "2021-12-08, Wed, 10:00" and returns the name of the weekday
# 3 days after the received date. For example, for the input provided, the output
# should be: Saturday.


some_date = "2021-12-08, Wed, 10:00"
def date_to_day():
    val = datetime.datetime.strptime(some_date, "%Y-%m-%d, %a, %H:%M")
    ret_val = val + datetime.timedelta(days=3)
    return datetime.datetime.strftime(ret_val, "%A")

res = date_to_day()

print(res)


# Implement a function that receives a date in format like the following:
# Mon, Dec 19, 2022 10:00 PM
# and returns the amount of time left until the provided date.
# The function should return a timedelta object.


date_insert = "Tue, Jan 31, 2023 10:00 PM"
def check_time_left():
    a = datetime.datetime.strptime(date_insert, "%a, %b %d, %Y %H:%M %p")
    b = datetime.datetime.strptime("Sun, Jan 30, 2023 10:00 PM", "%a, %b %d, %Y %H:%M %p")
    c = dt.strftime(b, "%a, %b %d, %Y %H:%M %p")
    ret_val = a - b
    return ret_val

print(check_time_left())



# Write a function that receives a date string in format dd-mm-yy,
# and returns a date of the upcoming Friday as string in format: dd-mm-yyyy

some_date = input("insert date")
def conv_date(some_date: str) -> str:
    val = datetime.datetime.strptime(some_date, "%d-%m-%y")
    val1 = val.isoweekday()
    val2 = 5 - val1
    ret_val = val + datetime.timedelta(days=val2)
    return ret_val.strftime("%d-%m-%Y"), ret_val.strftime("%A")
# date as a string
# need to get the day and replace by friday
# need to convert the date to string and calculate two dates till friday

res = conv_date(some_date)
print(res)


# Implement a function that receives a time in format hh:mm that represents the time when
# the lecture ends, and returns the amount of time left to the end of the lecture.

endtime = input("insert time when the lecture ends hh:mm")
def time_till_end():
    end_time = datetime.datetime.strptime(endtime, "%H:%M")
    now_time = datetime.datetime.now()
    time_remaining = end_time - now_time
    return time_remaining


print(time_till_end())



# Implement a function that does not receive any argument, and
# returns the amount of days left until the end of the current year.


def remain_end_year():
    now_date = datetime.date.today()
    end_year = now_date.replace(day=31, month=12)
    ret_val = end_year - now_date
    return ret_val

print(remain_end_year())
