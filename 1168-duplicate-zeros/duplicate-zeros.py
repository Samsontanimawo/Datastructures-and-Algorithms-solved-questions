class Solution(object):
    def duplicateZeros(self, arr):
        length = len(arr)
    
    # Iterate in reverse order
        for index in range(length - 1, -1, -1):
        # Duplicate zeros and shift elements to the right
            if arr[index] == 0:
                if index + 1 < length:
                    arr[index + 1:] = arr[index:-1]

                if index + 1 < length:
                    arr[index + 1] = 0