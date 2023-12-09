class Solution:
    def topKFrequent(self, nums, k):
        
        freq = Counter(nums)
        unique = list(freq.keys())
        k = len(unique)-k
        
        def quickSelect(left, right):
            pivot = unique[right]
            partition = left
            
            for index in range(left, right):
                if freq[unique[index]] <= freq[pivot]:
                    unique[index], unique[partition] = unique[partition], unique[index]
                    partition +=1
                    
            unique[partition], unique[right] = unique[right], unique[partition]
            
            if partition > k:
                return quickSelect(left, partition - 1)
            
            elif partition < k:
                return quickSelect(partition + 1, right)
            
            else:
                return unique[partition]
            
        quickSelect(0, len(unique)-1)
        return unique[k:]
    
    
    """
    O(N) TIME
    O(1) SPACE
    """