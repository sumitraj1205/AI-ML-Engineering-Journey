# Problem: Asteroid Collision
# Approach: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            alive = True

            while stack and stack[-1] > 0 and asteroid < 0:

                if stack[-1] < abs(asteroid):
                    stack.pop()

                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    alive = False
                    break

                else:
                    alive = False
                    break

            if alive:
                stack.append(asteroid)

        return stack


s = Solution()
print(s.asteroidCollision([5, 10, -5]))

print(s.asteroidCollision([8, -8]))