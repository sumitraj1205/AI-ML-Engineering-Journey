# 2Sum Problem
#
# Problem:
# Given an array of integers and a target value,
# find two elements whose sum is equal to the target.
#
# Return the indices of the two elements.
#
# Approach:
# Use a hash map to store elements that have already been visited.
#
# For every element:
# 1. Calculate the required value:
#    required = target - current element
# 2. Check whether the required value exists in the hash map.
# 3. If it exists, return the two indices.
# 4. Otherwise, store the current element and its index.
#
# Time Complexity: O(n) average
# Space Complexity: O(n)


def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):
        required = target - arr[i]

        if required in seen:
            return [seen[required], i]

        seen[arr[i]] = i

    return []


arr = [2, 6, 5, 8, 11]
target = 14

print(two_sum(arr, target))