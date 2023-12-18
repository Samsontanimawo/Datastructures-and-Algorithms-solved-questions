class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort()
        
        start, end, result = 1, -1, []

        for interval in intervals:
            if result == [] or result[end][start] < interval[0]:
                result.append(interval)

            else:
                result[end][start] = max(result[end][start], interval[end])

        return result