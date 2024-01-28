class Solution(object):
    def isCompleteTree(self, root):
        if not root:
            return True

        queue = [root]
        foundNull = False

        while queue:
            current = queue.pop(0)

            if current:
                if foundNull:
                    return False

                queue.append(current.left)
                queue.append(current.right)
            else:
                foundNull = True

        return True