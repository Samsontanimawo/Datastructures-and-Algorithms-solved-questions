class Solution(object):
    def lowestCommonAncestor(self, p, q):
        pCopy = p
        qCopy = q

        if pCopy.parent == qCopy.parent:
            return pCopy.parent or qCopy.parent

        while pCopy != qCopy:
            pCopy = pCopy.parent if pCopy else q
            qCopy = qCopy.parent if qCopy else p

        return pCopy or qCopy

# O(N) time
# O(1) space