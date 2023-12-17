class Solution(object):
    def deleteDuplicates(self, head):
        
        currentList = head

        while currentList and currentList.next:
            if currentList.val == currentList.next.val:
                currentList.next = currentList.next.next

            else:
                currentList = currentList.next

        return head