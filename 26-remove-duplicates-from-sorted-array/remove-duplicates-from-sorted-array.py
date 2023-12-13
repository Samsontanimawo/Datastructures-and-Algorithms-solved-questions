class Solution(object):
    def removeDuplicates(self, nums):
        left = 0

        while left < len(nums)-1:
            if nums[left] == nums[left + 1]:
                del nums[left]
            
            else:
                left +=1

        return len(nums)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#            L