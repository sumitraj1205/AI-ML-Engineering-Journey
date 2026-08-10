tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

combined = tuple1 + tuple2

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Combined:", combined)

print("Repeated:", tuple1 * 2)

print("20 exists:", 20 in tuple1)
print("100 exists:", 100 in tuple1)

print("Length:", len(combined))
print("Maximum:", max(combined))
print("Minimum:", min(combined))
print("Sum:", sum(combined))

print("First three:", combined[:3])
print("Last three:", combined[-3:])

list1 = [1, 2, 3, 4]

tuple3 = tuple(list1)

print("List:", list1)
print("Tuple:", tuple3)

tuple4 = (5, 6, 7, 8)

list2 = list(tuple4)

print("Tuple:", tuple4)
print("List:", list2)