class Solution(object):
    def deleteDuplicates(self, head):
        
        p1 = head

        while p1 and p1.next:
            if p1.val == p1.next.val:
                p1.next = p1.next.next

            else:
                p1 = p1.next

        return head