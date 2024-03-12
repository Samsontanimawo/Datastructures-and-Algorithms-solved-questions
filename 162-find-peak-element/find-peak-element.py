# Peak number is a number that's bigger than its neighbor

class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right)//2 
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            else:
                right = mid

        return left 

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(Solution().findPeakElement(test))