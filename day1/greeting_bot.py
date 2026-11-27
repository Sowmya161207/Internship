import datetime
import random
print("===============================")
print("WELCOME!!")
print("===============================")
quotes=["Believe in yourself","Every day is a new oppurtunity","success come from hard work"]
quote=random.choice(quotes)
print(f"quote of the day:{quote}")
name=input("Enter your name:")
if name=="":
    print("Enter a valid name!!")
else:
    hour=datetime.datetime.now().hour
    if hour<12:
        greeting="Good Morning"
    elif hour<17:
        greeting="Good Afternoon"
    else:
        greeting="Good evening"
    print(f"{greeting}! {name}")
    print("Welcome to your greeting bot!")
    goal=input("Enter your goal of the day:")
    print()
    print("===========Summary==========")
    print(f"Name:{name}")
    print(f"greeting:{greeting}")
    print(f"Goal:{goal}")
