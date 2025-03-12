class Solution(object):
    def deleteDuplicates(self, head):
        currentNode = head

        while currentNode and currentNode.next:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next

            else:
                currentNode = currentNode.next

        return head