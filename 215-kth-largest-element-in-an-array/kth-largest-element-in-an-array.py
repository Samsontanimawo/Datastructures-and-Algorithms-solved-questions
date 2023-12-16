import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        # Create an empty min heap to keep track of the k largest elements
        min_heap = []

        # Iterate through the elements in the input list
        for num in nums:
            # Push the negative of the element onto the min heap
            # (using negative values to simulate a max heap)
            heapq.heappush(min_heap, num)

            # If the size of the heap exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The top of the heap now contains the kth largest element
        return min_heap[0] # 0 is the top number of the heap