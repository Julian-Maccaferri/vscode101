from datetime import date

def hello(name):
    print(f"Hello, {name}!")

hello("VS Code!")

def say_day_of_week(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = days[date.weekday()]
    print(f"Today is {day_of_week}.")

say_day_of_week(date.today())

