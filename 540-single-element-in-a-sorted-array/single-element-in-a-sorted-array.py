class Solution(object):
    def singleNonDuplicate(self, nums):
        result = 0

        for num in nums:
            result = num ^ result

        return result

        # O(N) TIME | o(1) space
        