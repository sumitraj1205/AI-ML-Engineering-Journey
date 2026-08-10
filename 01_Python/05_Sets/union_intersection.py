set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference set1 - set2:", set1.difference(set2))
print("Difference set2 - set1:", set2.difference(set1))
print("Symmetric Difference:", set1.symmetric_difference(set2))

print("Union using |:", set1 | set2)
print("Intersection using &:", set1 & set2)
print("Difference using -:", set1 - set2)
print("Symmetric Difference using ^:", set1 ^ set2)