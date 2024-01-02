class Solution(object):
    def simplifyPath(self, path):
        paths = path.split("/")

        if not path:
            return []

        stack = []

        for path in paths:
            if not path or path == ".":
                continue

            elif path == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(path)

        return "/" + "/".join(stack)