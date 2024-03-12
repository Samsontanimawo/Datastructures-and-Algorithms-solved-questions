class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2 
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
    print(Solution().findPeakElement(test))