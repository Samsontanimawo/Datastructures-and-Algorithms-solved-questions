class Solution(object):
    def findDuplicate(self, nums):
        duplicate = set()

        for num in nums:
            if num in duplicate:
                return num

            else:
                duplicate.add(num)

        return num