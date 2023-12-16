class Solution(object):
    def isStrobogrammatic(self, num):
        
        rotatedDigits = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        left, right = 0, len(num)-1
        
        while left <= right:
            if num[left] not in rotatedDigits or rotatedDigits[num[left]] != num[right]:
                return False
            
            left +=1
            right -=1
        
        return True
    
    """
    O(N) Time
    O(1) Space
    """