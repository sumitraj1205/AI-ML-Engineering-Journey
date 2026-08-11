text = input("Enter a string: ")

text = text.lower()

reverse = text[::-1]

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")