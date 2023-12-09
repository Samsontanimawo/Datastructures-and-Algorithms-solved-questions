class SparseVector:
    def __init__(self, nums):
        # Store the indices and values of non-zero elements in a dictionary
        self.sparse_dict = {i: nums[i] for i in range(len(nums)) if nums[i] != 0}

    def dotProduct(self, vec):
        # Iterate through the indices and values of non-zero elements in both vectors
        result = 0
        for i, val in self.sparse_dict.items():
            if i in vec.sparse_dict:
                result += val * vec.sparse_dict[i]
        return result

# Example usage:
#nums1 = [1, 0, 0, 2, 3]
#nums2 = [0, 3, 0, 4, 0]

#v1 = SparseVector(nums1)
#v2 = SparseVector(nums2)

#print(v1.dotProduct(v2))  # Output: 8
