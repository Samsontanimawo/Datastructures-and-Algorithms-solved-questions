class Solution(object):
    def findDisappearedNumbers(self, nums):
        missingNumbers = set(nums)

        result = []

        for num in range(1, len(nums)+1):
            if num not in missingNumbers:
                result.append(num)

        return result