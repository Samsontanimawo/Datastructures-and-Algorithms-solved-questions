class Solution(object):
    def findDuplicate(self, nums):
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return num

            else:
                hashmap[num] = 1

        return len(num)