class Solution(object):
    def containsDuplicate(self, nums):
        # Create an empty dictionary to store the frequency of each number.
        hashmap = {}    # { 1  2 3 4 5 }

        # Iterate through the list of numbers.
        for num in nums:
            # Check if the number is already in the dictionary.
            # E.g [ 1,1,2,4,5,5 ] = new dict = [         ]
            if num in hashmap:
                # If the number is already in the dictionary, it means it's a duplicate.
                return True
            else:
                # If the number is not in the dictionary, add it with a frequency of 1.
                hashmap[num] = 1

        # If the loop completes without finding any duplicates, return False.
        return False
