class Solution:

    def __init__(self, weights):
        self.hashmap = []
        cummulativeSum = 0
        
        for weight in weights:
            cummulativeSum += weight
            self.hashmap.append(cummulativeSum)
            
        self.totalSum = cummulativeSum
        

    def pickIndex(self):
        randomNumber = self.totalSum * random.random()
        
        left, right = 0, len(self.hashmap)
        
        while left < right:
            mid = (left + right)//2
            
            if randomNumber > self.hashmap[mid]:
                left = mid + 1
                
            else:
                right = mid
                
        return right