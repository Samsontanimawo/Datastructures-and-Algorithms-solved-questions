class Solution(object):
    def merge(self, intervals):

        intervals.sort()

        if not intervals:
            return []

        result = []
        start, end = 1, -1

        for interval in intervals:
            if not result or result[end][start] < interval[0]:
                result.append(interval)

            else:
                result[end][start] = max(result[end][start], interval[end])

        return result