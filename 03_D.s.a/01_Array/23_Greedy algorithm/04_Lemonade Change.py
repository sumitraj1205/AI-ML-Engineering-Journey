# Problem: Lemonade Change
# Approach: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def lemonadeChange(self, bills):
        five = 0
        ten = 0

        for bill in bills:

            if bill == 5:
                five += 1

            elif bill == 10:
                if five == 0:
                    return False

                five -= 1
                ten += 1

            else:  # bill == 20

                # Prefer 10 + 5
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1

                # Otherwise use 5 + 5 + 5
                elif five >= 3:
                    five -= 3

                else:
                    return False

        return True


s = Solution()
print(s.lemonadeChange([5, 5, 5, 10, 20]))


print(s.lemonadeChange([5, 5, 10, 10, 20]))
