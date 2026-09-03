# Rearrange Array in Alternating Positive and Negative Items
#
# Problem:
# Rearrange an array so that positive and negative elements
# appear alternately.
#
# Example:
# Input  -> [3, 1, -2, -5, 2, -4]
# Output -> [3, -2, 1, -5, 2, -4]
#
# Approach:
# Store positive and negative elements separately.
#
# Then place:
# - Positive elements at even indices.
# - Negative elements at odd indices.
#
# This approach assumes that the number of positive and negative
# elements is suitable for alternating arrangement.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def rearrange(arr):
    positive = []
    negative = []

    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)

    result = []

    for i in range(min(len(positive), len(negative))):
        result.append(positive[i])
        result.append(negative[i])

    result.extend(positive[len(negative):])
    result.extend(negative[len(positive):])

    return result


arr = [3, 1, -2, -5, 2, -4]

print(rearrange(arr))