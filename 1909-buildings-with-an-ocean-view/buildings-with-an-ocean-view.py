#heights = [4,2,3,1]
# maxHeight = 1
# result = [ 1 3        ]

class Solution(object):
    def findBuildings(self, heights):
        maxHeight = 0
        result = []

        if not heights:
            return 0

        for index in range(len(heights)-1,-1,-1):
            if heights[index] > maxHeight:
                result.append(index)
                maxHeight = heights[index]

        return result[::-1]