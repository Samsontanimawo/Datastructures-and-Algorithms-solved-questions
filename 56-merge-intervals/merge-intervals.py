class Solution:
    def merge(self, intervals):

        if not intervals:
            return []

        # Define indices for start and end in the interval tuples
        start, end, result = 1, -1, []
        
        # Sort the intervals based on their start times
        intervals.sort()
        
        # Iterate through the sorted intervals
        for interval in intervals:
            # If the result is empty or the current interval does not overlap with the last merged interval
            if result == [] or result[end][start] < interval[0]:
                # Add the non-overlapping interval to the result
                result.append(interval)
            else:
                # Merge the overlapping intervals by updating the end of the last merged interval
                result[end][start] = max(result[end][start], interval[end])
                
        return result

# Example usage:
#solution = Solution()
#intervals1 = [[1,3],[2,6],[8,10],[15,18]]
#print(solution.merge(intervals1))  # Output: [[1,6],[8,10],[15,18]]

#intervals2 = [[1,4],[4,5]]
#print(solution.merge(intervals2))  # Output: [[1,5]]