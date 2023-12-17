class Solution(object):
    def duplicateZeros(self, arr):
        length = len(arr)
    
    # Iterate in reverse order
        for i in range(length - 1, -1, -1):
        # Duplicate zeros and shift elements to the right
            if arr[i] == 0:
                if i + 1 < length:
                    arr[i + 1:] = arr[i:-1]
                if i + 1 < length:
                    arr[i + 1] = 0
