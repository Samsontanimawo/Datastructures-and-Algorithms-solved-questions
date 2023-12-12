
# Input: heights = [4,   2,    3,   1]
# Index             0    1     2    3
# Output: [0,2,3]

# maxHeight = 3
# Result = [  4 3 1 ]



class Solution(object):
    def findBuildings(self, heights):
        if not heights:
            return []

        result = []
        maxHeight = 0

        for index in range(len(heights)-1,-1,-1):
            if heights[index] > maxHeight:
                result.append(index)
                maxHeight = heights[index]

        return result[::-1]