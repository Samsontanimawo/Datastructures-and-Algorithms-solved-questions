class Solution(object):
    def depthSum(self, nestedList):
        def helper(nestedList, depth):
            # Initialize the total sum for this level
            total_sum = 0

            # Iterate through each element in the current nested list
            for item in nestedList:
                # Check if the item is an integer
                if item.isInteger():
                    # If it's an integer, add its value multiplied by the depth to the total sum
                    total_sum += item.getInteger() * depth
                else:
                    # If it's a nested list, recursively call the helper function with increased depth
                    total_sum += helper(item.getList(), depth + 1)

            # Return the total sum for the current level
            return total_sum

        # Start the recursive process with an initial depth of 1
        return helper(nestedList, 1)
