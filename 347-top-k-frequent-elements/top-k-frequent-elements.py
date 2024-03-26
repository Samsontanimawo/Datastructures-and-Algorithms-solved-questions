from collections import *

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count the frequency of each element in the input list
        freq = Counter(nums)
        
        # Step 2: Create a list of unique elements
        nums = list(freq.keys())
        # nums = [num for num in freq.keys()]

        
        # Calculate the position where the kth frequent element would be in the sorted list
        k = len(nums) - k
        
        # Step 3: Define a helper function for quick selection
        def quickSelect(left, right):
            # Choose the pivot element (rightmost element in this case)
            pivot = nums[right]
            partition = left
            
            # Partition the nums list based on the frequency of elements
            for index in range(left, right):
                if freq[nums[index]] <= freq[pivot]:
                    nums[index], nums[partition] = nums[partition], nums[index]
                    partition += 1
                    
            # Move the pivot element to its final sorted position
            nums[partition], nums[right] = nums[right], nums[partition]
            
            # Recursively perform quick select on the appropriate partition
            if partition > k:
                return quickSelect(left, partition - 1)

            elif partition < k:
                return quickSelect(partition + 1, right)

            else:
                return nums[partition]
            
        # Step 4: Perform quick selection to find the kth frequent element
        quickSelect(0, len(nums) - 1)
        
        # Step 5: Return the top k frequent elements
        return nums[k:]

# Additional information in comments
"""
O(N) TIME
O(N) SPACE
"""
