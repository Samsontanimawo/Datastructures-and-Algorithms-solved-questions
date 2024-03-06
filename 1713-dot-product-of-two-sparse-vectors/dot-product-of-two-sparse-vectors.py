class SparseVector:
    def __init__(self, nums):
        self.tuple = []
        
        for index, num in enumerate(nums):
            self.tuple.append((index, num))
        

    
    def dotProduct(self, vector):
        
        dotProduct = left = right = 0
        
        while left < len(self.tuple) and right < len(vector.tuple):
            leftIndex, leftNum = self.tuple[left]
            rightIndex, rightNum = vector.tuple[right]
            
            if leftIndex == rightIndex:
                dotProduct += leftNum * rightNum
                left +=1
                right +=1
                
            elif leftIndex < rightIndex:
                left +=1
                
            else:
                right -=1
                
        return dotProduct
    
    """
    O(N) Time | O(1) Space
    """