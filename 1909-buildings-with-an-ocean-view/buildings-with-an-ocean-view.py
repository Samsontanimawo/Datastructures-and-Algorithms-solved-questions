class Solution(object):
    def findBuildings(self, heights):
       maxHeight, result = 0, []

       for index in range(len(heights)-1,-1,-1):
         if maxHeight < heights[index]:
           result.append(index)
           maxHeight = heights[index]

       return result[::-1] 