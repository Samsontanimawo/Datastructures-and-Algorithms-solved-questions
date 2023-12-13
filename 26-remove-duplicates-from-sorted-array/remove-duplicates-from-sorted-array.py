class Solution(object):
    def removeDuplicates(self, nums):
        left = 0

        while left < len(nums)-1:
            if nums[left] == nums[left + 1]:
                del nums[left]

            else:
                left +=1
              

        return len(nums) # The output will be the length of the numbers. E.g 5

# Example usage
#nums = [1, 1, 2, 2, 4, 4, 5]
#result = Solution().removeDuplicates(nums)
#print(result)

# nums = [1, 1, 2, 2, 4, 4, 5]
 #            L
# Indices 0  1  2  3  4  5  6

# [   1 2 4 5 ]