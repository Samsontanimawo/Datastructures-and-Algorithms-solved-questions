class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        left = 0

        while left < len(nums)-1:
            if nums[left] == nums[left + 1]:
                return True

            else:
                left +=1

        return False