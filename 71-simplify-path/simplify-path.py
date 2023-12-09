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

# The canonical path should have the following format:

# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.