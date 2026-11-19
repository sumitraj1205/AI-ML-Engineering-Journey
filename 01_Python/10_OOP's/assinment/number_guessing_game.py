import random
b = random.randint(1,100)
while(True):
    a = float(input("enter the number"))
    if(a == b):
        print("correct guess")
        break
    elif(a>b):
        print("guess lower")
    else:
        print("guess higher")