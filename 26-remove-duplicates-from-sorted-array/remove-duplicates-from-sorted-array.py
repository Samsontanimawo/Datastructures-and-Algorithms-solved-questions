class Solution(object):
    def removeDuplicates(self, nums):
        left = 0

        while left < len(nums)-1:
            if nums[left] == nums[left + 1]:
                del nums[left + 1]

            else:
                left +=1

        return len(nums)