class Solution(object):
    def containsDuplicate(self, nums):
        duplicate = {}

        for num in nums:
            if num in duplicate:
                return True

            else:
                duplicate[num] = 1

        return False