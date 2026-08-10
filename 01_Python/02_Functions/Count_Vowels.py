def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count


text = input("Enter a sentence: ")

print("Number of vowels =", count_vowels(text))