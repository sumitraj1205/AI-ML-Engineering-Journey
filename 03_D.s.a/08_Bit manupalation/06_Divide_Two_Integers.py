# Problem: Divide two integers without using *, / or %.
# Approach: Use bit shifting and subtraction.
# Time Complexity: O(log^2 |dividend|) for this implementation.
# Space Complexity: O(1)

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # Determine the sign of the result
    negative = (dividend < 0) ^ (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    # Subtract the largest possible shifted divisor
    for i in range(dividend.bit_length() - divisor.bit_length(), -1, -1):
        if (divisor << i) <= dividend:
            dividend -= divisor << i
            quotient += 1 << i

    if negative:
        quotient = -quotient

    return quotient


dividend = 43
divisor = -5

print(divide(dividend, divisor))