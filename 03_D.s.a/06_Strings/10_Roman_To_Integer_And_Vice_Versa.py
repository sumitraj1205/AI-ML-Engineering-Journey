# Problem:
# Convert a Roman numeral to an integer and an integer to a Roman numeral.
#
# Approach:
# Roman to Integer:
# Store Roman symbols and their values in a dictionary.
# If a smaller value comes before a larger value, subtract it.
# Otherwise, add it.
#
# Integer to Roman:
# Store Roman values in decreasing order.
# Repeatedly take the largest possible value and add its symbol.
#
# Time Complexity:
# Roman to Integer: O(n)
# Integer to Roman: O(1)
#
# Space Complexity:
# Roman to Integer: O(1)
# Integer to Roman: O(1)


def roman_to_integer(s):
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]

    return total


def integer_to_roman(num):
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for value, symbol in values:
        while num >= value:
            result += symbol
            num -= value

    return result


roman = "MCMXCIV"
number = 1994

print("Roman to Integer:", roman_to_integer(roman))
print("Integer to Roman:", integer_to_roman(number))