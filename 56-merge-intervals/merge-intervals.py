class Solution(object):
    # Function to merge overlapping intervals
    def merge(self, intervals):
        # Check if the intervals list is empty
        if not intervals:
            return None  # If empty, return None
        
        start = 0  # Index of start time in interval
        end = 1    # Index of end time in interval
        result = []  # List to store the merged intervals

        intervals.sort()  # Sort the intervals based on start times

        # Loop through each interval in sorted intervals
        for interval in intervals:
            # Check if the result list is empty or the current interval starts after the end of the last interval in the result list
            if not result or result[-1][end] < interval[start]:
                result.append(interval)  # If so, add the current interval to the result list
                
            else:
                # If the current interval overlaps with the last interval in the result list, merge them
                result[-1][end] = max(result[-1][end], interval[end])  # Update the end time of the last interval in result list

        return result  # Return the merged intervals
