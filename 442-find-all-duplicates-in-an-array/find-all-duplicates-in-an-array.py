class Solution:
    def findDuplicates(self, nums):
        duplicates = []
        for num in nums:
            # Get the absolute value of the number as index
            index = abs(num) - 1
            # If the number at index is negative, it means it has been encountered before
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                # Mark the number at index as negative
                nums[index] = -nums[index]
        return duplicates

# Example usage:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
print(solution.findDuplicates(nums))  # Output: [2, 3]
