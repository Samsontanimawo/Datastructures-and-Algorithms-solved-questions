class Solution(object):
    def merge(self, intervals):
       if not intervals:
           return None

       start, end, result = 1, -1, []

       intervals.sort()

       for interval in intervals:
           if result == [] or result[end][start] < interval[0]:
               result.append(interval)

           else:
                result[end][start] = max(result[end][start], interval[end])

       return result

# nlogn time | O(N) space