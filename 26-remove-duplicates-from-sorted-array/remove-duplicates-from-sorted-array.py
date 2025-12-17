# nums =  [1, 2, 2, 3, 3,     4]
#          |  |               |
#          L  L+1             R

# [0,   1,    2,    3     4]
#                   |     |    
#                   L    L+1   
#                   R
# [0,   1,    2,    3     4]


class Solution(object):
    def removeDuplicates(self, nums):
        left, right = 0, len(nums)-1

        while left < len(nums)-1:
            if nums[left] == nums[left + 1]:
                del nums[left]

            else:
                left +=1
                right -=1

        return len(nums)
        