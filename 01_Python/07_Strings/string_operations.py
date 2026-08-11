text = input("Enter a string: ")

print("String:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())
print("Capitalized:", text.capitalize())
print("Swapcase:", text.swapcase())
print("Count of a:", text.count("a"))
print("Index of first character:", text.find(text[0]))
print("Starts with A:", text.startswith("A"))
print("Ends with a:", text.endswith("a"))

print("First character:", text[0])
print("Last character:", text[-1])
print("First three characters:", text[:3])
print("Last three characters:", text[-3:])
print("Reversed:", text[::-1])

print("Is alphabetic:", text.isalpha())
print("Is digit:", text.isdigit())
print("Is alphanumeric:", text.isalnum())
print("Is lowercase:", text.islower())
print("Is uppercase:", text.isupper())

words = text.split()
print("Words:", words)

new_text = "-".join(words)
print("Joined:", new_text)

print("Without spaces:", text.replace(" ", ""))