b = input("enter the value")
c = ""
for i in b[::-1]:
    c = c + i
if(c == b):
    print(f"{b} is a palindrome")
else:
    print(f"{b} is not a palindrome")
