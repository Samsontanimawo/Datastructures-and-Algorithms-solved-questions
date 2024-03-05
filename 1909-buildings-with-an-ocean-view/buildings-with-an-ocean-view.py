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

            else:
                continue

        return result[::-1]