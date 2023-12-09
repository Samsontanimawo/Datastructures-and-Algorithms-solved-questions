class Solution(object):
    def lowestCommonAncestor(self, p, q):
        # Make copies of the input nodes
        pCopy = p
        qCopy = q

        # Traverse upwards from the nodes until a common ancestor is found
        while pCopy != qCopy:
            # Move pCopy to its parent if it exists, otherwise, move it to q
            pCopy = pCopy.parent if pCopy else q
            # Move qCopy to its parent if it exists, otherwise, move it to p
            qCopy = qCopy.parent if qCopy else p

        # Return the common ancestor (either pCopy or qCopy)
        return pCopy or qCopy
