class Solution:
    def threeSum(self, nums):
        if not nums: return []
        nums.sort()
        threesome = list()
        
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                remaining = 0 - nums[i]
                left, right = i+1, len(nums)-1
                while left < right:
                    if remaining == (nums[left] + nums[right]):
                        threesome.append([nums[i], nums[left], nums[right]])
                        
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif remaining > nums[left] + nums[right]:
                        left += 1
                    else:
                        right -= 1
            
        return threesome