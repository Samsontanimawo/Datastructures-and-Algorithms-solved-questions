class Solution(object):
    def simplifyPath(self, path):
        if not path:
            return []

        stack = []


        paths = path.split("/")

        for path in paths:
            if path == "." or not path:
                continue

            elif path == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(path)

        return "/" + "/".join(stack)