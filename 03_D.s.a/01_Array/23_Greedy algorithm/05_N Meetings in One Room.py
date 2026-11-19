# Problem: N Meetings in One Room
# Approach: Greedy + Sorting by ending time
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def maxMeetings(self, start, end):
        n = len(start)

        meetings = []

        for i in range(n):
            meetings.append((start[i], end[i], i + 1))

        # Sort according to ending time
        meetings.sort(key=lambda x: x[1])

        count = 0
        last_end = -1
        selected = []

        for s, e, index in meetings:
            if s > last_end:
                count += 1
                selected.append(index)
                last_end = e

        return count


s = Solution()
print(s.maxMeetings([1, 3, 0, 5, 8, 5],
                    [2, 4, 6, 7, 9, 9]))