class Solution(object):
    def lowestCommonAncestor(self, p, q):
        # Create copies of the input nodes
        pCopy = p
        qCopy = q

        # Check if the input nodes are the same
        if pCopy == qCopy:
            # If so, return the parent of either node (assuming they have a 'parent' attribute)
            return pCopy.parent or qCopy.parent

        # Iterate until the nodes reach the same ancestor or are both None
        while pCopy != qCopy:
            # Move to the parent of node pCopy if it is not None, otherwise, use node q
            pCopy = pCopy.parent if pCopy else q
            # Move to the parent of node qCopy if it is not None, otherwise, use node p
            qCopy = qCopy.parent if qCopy else p

        # Return the common ancestor (or None if there is no common ancestor)
        return qCopy or pCopy
