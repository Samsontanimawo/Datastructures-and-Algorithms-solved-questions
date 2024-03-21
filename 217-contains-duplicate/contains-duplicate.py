class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()

        left = 0
        right = len(nums)-1

        while left < len(nums)-1:
            if nums[left] == nums[left + 1]:
                return True

            else:
                left +=1
                right -=1

        return False

# O(nlogN) time = Sorting 
# O(1) SPACE