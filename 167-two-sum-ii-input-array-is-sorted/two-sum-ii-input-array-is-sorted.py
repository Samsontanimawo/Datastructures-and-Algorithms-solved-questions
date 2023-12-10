class Solution(object):
    def twoSum(self, nums, target):
        left, right = 0, len(nums)-1

        while left < right:
            sum = nums[left] + nums[right]

            if sum == target:
                return [left + 1, right + 1]

            elif sum < target:
                left +=1

            else:
                right -=1

