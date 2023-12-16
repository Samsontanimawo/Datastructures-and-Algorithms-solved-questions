class Solution(object):
    def findBuildings(self, heights):
        result = []
        maxHeight = 0

        for index in range(len(heights)-1,-1,-1):
            if heights[index] > maxHeight:
                result.append(index)
                maxHeight = heights[index]

        return result[::-1]

# O(N) Time and space