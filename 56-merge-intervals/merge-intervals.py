class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        start, end, result = 1, -1, []
        
        intervals.sort()
        
        for interval in intervals:
            if result == [] or result[end][start] < interval[0]:
                result.append(interval)
                
            else:
                result[end][start] = max(result[end][start], interval[start])
                
        return result