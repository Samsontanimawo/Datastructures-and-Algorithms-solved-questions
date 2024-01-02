class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return None

        intervals.sort()

        start, end = 1, -1
        result = []

        for interval in intervals:
            if not result or result[end][start] < interval[0]:
                result.append(interval)

            else:
                result[end][start] = max(result[end][start], interval[end])

        return result