class Solution(object):
    def depthSum(self, nestedList):
        # Define a helper function for depth-sum calculation
        def helper(nestedList, depth):
            # Initialize the sum to 0
            sum = 0

            # Iterate through each element in the nestedList
            for item in nestedList:
                # If the current item is an integer
                if item.isInteger():
                    # Add the integer value multiplied by the current depth to the sum
                    sum += item.getInteger() * depth 

                # If the current item is a nested list
                else:
                    # Recursively call the helper function with the nested list and incremented depth
                    sum += helper(item.getList(), depth + 1)

            # Return the sum calculated for the current nestedList
            return sum

        # Start the depth-sum calculation with the input nestedList and initial depth of 1
        return helper(nestedList, 1)
