class Solution:
    def simplifyPath(self, path):
        # Split the path using '/'
        paths = path.split("/")
        stack = []

        # Ignore empty and '.' components
        for char in paths:
            if char == "." or not char:
                continue

            # Handle '..' by popping the last directory from the stack (if not empty)
            elif char == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(char)

        # Construct the simplified canonical path by joining the directories with '/'
        return "/" + "/".join(stack)
