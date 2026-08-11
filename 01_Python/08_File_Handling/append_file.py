file = open("data.txt", "a")

text = input("Enter text to add: ")

file.write("\n" + text)

file.close()

print("Data added successfully.")