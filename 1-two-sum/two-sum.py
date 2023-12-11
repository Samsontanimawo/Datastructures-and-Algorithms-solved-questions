class Solution:
    def twoSum(self, nums, target):
        
        hashmap = {}
        
        for index, num in enumerate(nums):
            diff = target - nums[index]
            
            if diff in hashmap:
                return [hashmap[diff], index]
            
            else:
                hashmap[num] = index
                
                """
                O(N) Time and Space
                
                """
        