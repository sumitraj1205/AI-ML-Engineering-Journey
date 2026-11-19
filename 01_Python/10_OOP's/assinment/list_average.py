a = []
b = int(input("enter the number of elements in the list"))
c = 0
print("enter the values of the list")
for i in range(b):
    a.append(int(input()))
for i in a:
    c =c + i
d = c/b
print("avg = ",d)