class Solution(object):
    def minSwaps(self, data):
        ones_count = sum(data)  # Total count of 1s
        if ones_count == 0:
            return 0  # If there are no 1s, no swaps needed

        # Count zeros in the first window of size ones_count
        current_zeros = sum(1 for i in range(ones_count) if data[i] == 0)
        min_swaps = current_zeros  # Initialize minimum swaps with first window

        # Sliding window over the array
        for i in range(ones_count, len(data)):
            # Remove the leftmost element from the window
            if data[i - ones_count] == 0:
                current_zeros -= 1
            
            # Add the new element to the window
            if data[i] == 0:
                current_zeros += 1

            # Update the minimum swaps needed
            min_swaps = min(min_swaps, current_zeros)

        return min_swaps
