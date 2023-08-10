class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums)-k
        
        def quickSelect(left, right):
            partition = left
            pivot = nums[right]
            
            
            for index in range(left, right):
                if nums[index] <= pivot:
                    nums[partition], nums[index] = nums[index], nums[partition]
                    partition +=1
                    
            nums[partition], nums[right] = nums[right], nums[partition]
            
            if partition > k:
                return quickSelect(left, partition - 1)
            
            elif partition < k:
                return quickSelect(partition + 1, right)
            
            else:
                return nums[partition]
            
        return quickSelect(0, len(nums)-1)
        