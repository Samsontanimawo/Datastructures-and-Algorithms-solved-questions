class Solution(object):
    def simplifyPath(self, path):
        # Split the input path by "/" to get individual path components
        paths = path.split("/")
        # Initialize an empty stack to keep track of valid path components
        stack = []
        
        # Iterate through each path component
        for path in paths:
            # If the path component is "." or empty, skip to the next component
            if path == "." or not path:
                continue 

            # If the path component is "..", pop the last component from the stack (if the stack is not empty)
            elif path == "..":
                if stack:
                    stack.pop()

            # Otherwise, the path component is a valid directory name, so push it onto the stack
            else:
                stack.append(path)

        # Concatenate the valid path components in the stack with "/" separators and return the simplified path
        return "/"+"/".join(stack)
