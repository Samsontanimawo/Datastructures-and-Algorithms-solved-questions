# 1   2  3  4  5  6  7  8    9   0   1
#     L                          M                  R


class Solution(object):
    def findPeakElement(self, nums):
       left, right = 0, len(nums)-1

       while left < right:
           mid = (left + right)//2

           if nums[mid] < nums[mid + 1]:
               left = mid + 1

           else:
                right = mid

       return left



       