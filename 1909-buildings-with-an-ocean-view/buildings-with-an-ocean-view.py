class Solution(object):
    def findBuildings(self, heights):
        # Input: heights = [4,2,3,1]
#       Output: [0, 6, 2,3]
        # Result [     3]
        # MaxHeight = 6

        maxHeight, result = 0, []

        if not heights:
            return None

        for index in range(len(heights)-1, -1, -1):
            if heights[index] > maxHeight:
                result.append(index)
                maxHeight = heights[index]

        return result [::-1]