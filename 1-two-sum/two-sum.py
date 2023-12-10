class Solution(object):
    def twoSum(self, nums, target):
        # Enumerate the sorted array to keep track of the original indices.
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    
        # Initialize two pointers.
        left, right = 0, len(nums) - 1
    
        while left < right:
            current_sum = sorted_nums[left][1] + sorted_nums[right][1]
        
            # Check if the sum is equal to the target.
            if current_sum == target:
                # Return the original indices of the two numbers.
                return [sorted_nums[left][0], sorted_nums[right][0]]
        
        # If the sum is less than the target, move the left pointer to the right.
            elif current_sum < target:
                left += 1
        
        # If the sum is greater than the target, move the right pointer to the left.
            else:
                right -= 1

# Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# result = twoSum(nums, target)
# print(result)
