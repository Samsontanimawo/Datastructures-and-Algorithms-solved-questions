class Solution(object):
    def lowestCommonAncestor(self, p, q):
        pCopy = p
        qCopy = q

        if pCopy == qCopy:
            return pCopy.parent or qCopy.parent

        while pCopy != qCopy:
            pCopy = pCopy.parent if pCopy else q
            qCopy = qCopy.parent if qCopy else p

        return qCopy or pCopy

        