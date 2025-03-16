"""
Input: nums = [1,2,3,1]
Use set = [1, 2, 3]

return len(nums) != len(set(nums))

Time and Space Complexity Analysis
Time Complexity:
Creating a set from nums → set(nums) takes O(N) time, where N is the length of nums.
Computing len(nums) and len(set(nums)) → Both are O(1) operations.
Overall Complexity: O(N)
Space Complexity:
set(nums) stores unique elements → In the worst case, if all elements are distinct, the set will contain N elements.
Extra space used is O(N) for the set.
Overall Complexity: O(N)

"""


class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        