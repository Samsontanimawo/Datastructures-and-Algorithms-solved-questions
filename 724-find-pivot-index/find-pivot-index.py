# Input: nums = [1, 7, 3, 6, 5, 6]
# Index =        0  1  2  3  4  5
# Output: 3



# LeftSum = 1 + 7 + 3 + 6 = 11
# totalSum = 1 + 7 + 3 + 6 + 5 + 6 = 28
# 28 - 0 = 28
# 28-1 = 27
# 27 - 7 = 20
# 20 - 3 = 19
# 17 - 6 = 11
#totalSum = LeftSum = 11

class Solution(object):
  def pivotIndex(self, nums):
    totalSum = sum(nums)
    leftSum = 0

    for index in range(len(nums)):
      totalSum = totalSum - nums[index]

      if leftSum == totalSum:
        return index

      else:
        totalSum -= nums[index]

    return -1