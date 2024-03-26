class Solution(object):
    def shipWithinDays(self, weights, days):
        # Initialize left and right pointers for binary search
        left = max(weights)  # Minimum capacity required cannot be less than the weight of the heaviest package
        right = sum(weights)  # Maximum capacity required is the sum of all weights
        
        # Perform binary search until left pointer crosses right pointer
        while left < right:
            # Calculate the mid capacity
            mid = (left + right) // 2
            
            # Initialize variables to keep track of current weight and number of days needed
            curr_weight = 0
            curr_days = 1
            
            # Iterate through the weights to simulate shipping with the current capacity
            for weight in weights:
                # If adding the current weight exceeds the mid capacity, increment the number of days and reset the current weight
                if curr_weight + weight > mid:
                    curr_days += 1
                    curr_weight = 0
                
                # Add the current weight to the current weight
                curr_weight += weight
            
            # If the number of days exceeds the given days, adjust the left pointer to search in the higher capacity range
            if curr_days > days:
                left = mid + 1
            # Otherwise, adjust the right pointer to search in the lower capacity range
            else:
                right = mid
        
        # The least weight capacity that will result in all packages being shipped within the given days is left
        return left
