import random
a = random.randint(1,100)
i = 1
print("guess the number under 7 attempts to win a prize")
while(i<8):
    try:
        b = int(input("enter number-"))
        if b == a:
            print("you are the winer")
            print(f"you took {i} attempts")
            break
        elif b < a:
            print("guess highter")
        elif b > a:
            print("guess lower")
        i = i+ 1
        print(f"now you have {8-i} attempts")
    except ValueError:
        print("invalid choice , enter a valid choice")
if i == 8:
    print("you were not able to guess the number")
    print("the no. was-",a)