source = open("data.txt", "r")

data = source.read()

source.close()

destination = open("copy.txt", "w")

destination.write(data)

destination.close()

print("File copied successfully.")