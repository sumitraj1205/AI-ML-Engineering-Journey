def check_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


word = input("Enter a word: ")

if check_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")