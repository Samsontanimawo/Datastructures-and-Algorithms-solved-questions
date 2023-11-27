class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        
        left = right = 0 #word, abbr
        
        while left < len(word) and right < len(abbr):
            if word[left] != abbr[right]:
                if not abbr[right].isdigit():
                    return False
                
                else:
                    if abbr[right]== "0":
                        return False
                                        
                    
                    num = 0
                    
                    while right < len(abbr) and abbr[right].isdigit():
                        num = num * 10 + int(abbr[right])
                        right +=1
                    left += num
                    
            else:
                left +=1
                right +=1
                
        return left == len(word) and right == len(abbr)
    
    """
    O(N) TIME
    O(1) SPACE
    
    """