class Solution:
    def simplifyPath(self, path):
        
        paths = path.split("/")
        stack = []
        
        for char in paths:
            if char == "." or not char:
                continue
                
            elif char == "..":
                if stack:
                    stack.pop()
                    
            else:
                stack.append(char)
        
        return "/" + "/" ''.join(stack)
        