class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        start, end = 1, -1
        result = []

        intervals.sort()

        for interval in intervals:
            if result == [] or result[end][start] < interval[0]:
                result.append(interval)

            else:
                result[end][start] = max(result[end][start], interval[end])

        return result

# O(nlogN) time | O(1) Space
