list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)

common_list = list(common)

print("Common elements as list:", common_list)