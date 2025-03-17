class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Initialize two pointers: 'fast' and 'slow' both at the head of the list
        fast = slow = head

        # Move the 'fast' pointer 'n' steps ahead
        for index in range(n):
            fast = fast.next  # Move the fast pointer one step ahead
            # If n = 2, move the second pointer to position 2

        # If fast is None, it means the 'n'th node from the end is the head node
        # We just need to remove the head and return the new head
        if not fast:
            return slow.next  # Remove the head node and return the next node

        # Move both fast and slow pointers one step at a time
        # Now fast is 'n' nodes ahead, so when fast reaches the end,
        # slow will be at the node just before the one to be removed
        while fast.next:
            fast = fast.next  # Move the fast pointer one step forward
            slow = slow.next  # Move the slow pointer one step forward

        # Now, slow is at the node just before the one to be removed
        slow.next = slow.next.next  # Remove the 'n'th node from the end by skipping it

        # Return the head of the modified list
        return head

# Time Complexity: O(N), where N is the length of the linked list
# Space Complexity: O(1), because we are only using two pointers and not any additional space
