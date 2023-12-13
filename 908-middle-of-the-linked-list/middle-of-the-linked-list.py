class Solution(object):
    def middleNode(self, head):
        fast = slow = head # Both should start at the head

        while fast and fast.next: # Make sure fast and fast.next exist
            fast = fast.next.next # Fast moves 2 steps
            slow = slow.next # Slow moves 1 step

        return slow # Return slow = Middle number or right number