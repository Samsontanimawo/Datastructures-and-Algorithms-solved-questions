class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        all_numbers = set(range(1, n+1))
        num_set = set(nums)
        missing_numbers = list(all_numbers - num_set)
        return missing_numbers