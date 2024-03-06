class Solution(object):
    def simplifyPath(self, path):
        paths = path.split("/")
        stack = []
        
        for path in paths:
            if path == "." or not path:
                continue 

            elif path == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(path)


        return "/"+"/".join(stack)