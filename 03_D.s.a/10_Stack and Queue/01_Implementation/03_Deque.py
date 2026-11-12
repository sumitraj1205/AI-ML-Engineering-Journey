# Problem: Understand Deque in Python
# Approach: Use collections.deque
# Time Complexity: Append/Appendleft/Pop/Popleft O(1)
# Space Complexity: O(n)

from collections import deque

dq = deque()

# Insert elements
dq.append(10)       # Insert at right
dq.append(20)
dq.appendleft(5)    # Insert at left

print(dq)           # deque([5, 10, 20])

# Remove elements
dq.pop()            # Remove from right
dq.popleft()        # Remove from left

print(dq)           # deque([10])

# Access elements
print(dq[0])        