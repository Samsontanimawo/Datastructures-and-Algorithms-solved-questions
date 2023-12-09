class Solution(object):
    def findBuildings(self, heights):
        # Initialize variables to keep track of the maximum height and the result list
        maxHeight, result = 0, []

        # Check if the input list is empty
        if not heights:
            return None

        # Iterate through the heights in reverse order (from right to left)
        for index in range(len(heights) - 1, -1, -1):

            # Check if the current building is taller than the previous maximum height
            if heights[index] > maxHeight:

                # If yes, add the index to the result list and update the maximum height
                result.append(index)
                maxHeight = heights[index]

        # Reverse the result list to obtain the order from left to right
        return result[::-1] # Result = [ 4 3 1 ] = [1 3 4] = Return the index = [0, 2, 3]

# Example usage:
#solution_instance = Solution()
#result = solution_instance.findBuildings([4, 2, 3, 1])
#print(result)

