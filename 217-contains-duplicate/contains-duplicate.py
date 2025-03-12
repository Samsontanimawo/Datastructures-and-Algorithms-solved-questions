class Solution(object):
    def containsDuplicate(self, nums):
        duplicate = set()

        for num in nums:
            if num in duplicate:
                return True

            else:
                duplicate.add(num)

        return False