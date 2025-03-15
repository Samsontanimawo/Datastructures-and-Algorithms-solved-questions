# What is a peak element?
# Return the index of any of the peaks
# Input: nums = [1,2,3,1] | nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# # Output = 3 | 9
# How can we solve this problem?
# This is array related problem
# Sort the numbers and return the largest. Nums.sort(), return nums[-1]
#
#
#
#
#
class Solution(object):
    def findPeakElement(self, nums):
        sorted_nums = sorted(nums)  # Sort a copy to avoid modifying the original
        peak_value = sorted_nums[-1]  # Get the largest element (a peak)
        return nums.index(peak_value) 