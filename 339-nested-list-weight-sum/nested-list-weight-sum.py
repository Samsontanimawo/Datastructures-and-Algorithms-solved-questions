class Solution(object):
    def depthSum(self, nestedList):
        def helper(nestedList, depth):
            sum = 0
            
            for item in nestedList:
                if item.isInteger():
                    sum += item.getInteger() * depth

                else:
                    sum += helper(item.getList(), depth+1)

            return sum

        return helper(nestedList, 1)