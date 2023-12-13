class Solution:
    def removeNthFromEnd(self, head, n):
        
        slow = fast = head
        
        for index in range(n):
            fast = fast.next 
            
        if not fast:
            return slow.next 

        while fast.next:
            fast = fast.next 
            slow = slow.next 

        slow.next = slow.next.next 
            
        return head 