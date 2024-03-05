import random
import time
a = 0
b = 100
c = 123
futile = False
while futile == False:
    time.sleep(1)
    getgo = str(input("Continue? (y/n)\n"))
    if getgo == "y":
        d = int(input(f"Pick a number between {a} and {b}\n"))
        if d < a or d > b:
            print(f"ERROR: not between {a} or {b}\n")
        else:
            time.sleep(1)
            print(f"TEST{a+b+c}\n")
        a = random.randint(0,10)
        b = random.randint(90, 110)
        c = random.randint(101,123)
    else:
        print("You lost.\n")
        futile = True

time.sleep(5)
print(f"TEST{c-b}\n")
c = random.randint(101,123)
time.sleep(2)
print(f"So you are still here...\n")
time.sleep(2)
print(f"PHASE 2 INITALISE\n")
time.sleep(1)
user = str(input(f"TEST{(c-b)^2}\nInsert Username\n"))
if user != "kyle":
    futile = False
else:
    pin = int(input("Insert pin\n"))
    if pin != (c+c)/(c*2):
        time.sleep(2)
        futile = False
    else:
        time.sleep(2)
        print("Welcome agent GARRY FISHER")
