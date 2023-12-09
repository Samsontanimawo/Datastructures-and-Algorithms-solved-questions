class Solution:
    def removeInvalidParentheses(self, s) :        
        redundant_open=0
        redundat_close=0
        
        for char in s:
            if char =="(":
                redundant_open+=1
                
            elif char ==")":
                if redundant_open>0:
                    redundant_open-=1
                    
                else:				        

                    redundat_close+=1
        
        result = set()
        
        def helper(index,left,right,openP,close,valid):		    
            if index==len(s):
                if left==right and openP==0 and close==0:
                    result.add(valid)
                return 
            
            if s[index]=='(':
                if openP>0:
                    helper(index+1,left,right,openP-1,close,valid)
                    
                helper(index+1,left+1,right,openP,close,valid+"(")
                
            elif s[index]==')':
                if close>0:
                    helper(index+1,left,right,openP,close-1,valid)
                if  right<left:  
                    helper(index+1,left,right+1,openP,close,valid+")")
            else:
                helper(index+1,left,right,openP,close,valid+s[index])             
        
        helper(0,0,0,redundant_open,redundat_close,"")
        return list(result)     
#TC= O(2**N)
