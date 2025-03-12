class Solution(object):
    def findDuplicate(self, nums):
        duplicate = {}

        for num in nums:
            if num in duplicate:
                return num

            else:
                duplicate[num] = 1

        return num