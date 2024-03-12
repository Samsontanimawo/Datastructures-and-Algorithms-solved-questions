
# MOVE ZEROS TO LEFT
# Input = [ 1, 0, 2, 0, 0, 0, 1]
# Ouput = [0, 0, 0, 0, 1, 1, 2]


# MOVE ZEROS TO RIGHT
# Ouput = [0, 0, 0, 0, 1, 1, 2]
# Input = [ 1, 1, 2, 0, 0, 0, 0]

class Solution(object):
  def move_zeros_to_left_and_right(self, nums):
    left = len(nums) - 1
    right = len(nums)-1

    while left >= 0:
 #   while left >= 0: # Replace right with left if you want the zeros to move to right 
      if nums[right] != 0:
        nums[right], nums[left] = nums[left], nums[right]
        left -=1

      right -=1

    return nums

test = [8, 0, 0, 0, 1, -3, 12]

print(Solution().move_zeros_to_left_and_right(test))