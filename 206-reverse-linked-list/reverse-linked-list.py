class Solution(object):
    def reverseList(self, head):
        newList = None
        currentList = head

        while currentList:
            nextNode = currentList.next
            currentList.next = newList
            newList = currentList
            currentList = nextNode

        return newList

