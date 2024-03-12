def remove_duplicates(arr):

    # Edge case: Empty array or array with only one element
    if not arr or len(arr) == 1:
        return arr

    next_unique = 1  # Position to place the next unique element

    # Iterate through the array starting from the second element
    for index in range(1, len(arr)):
      
        # If the current element is different from the previous one
        if arr[index] != arr[index - 1]:
            # Move the current element to the position indicated by next_unique
            arr[next_unique] = arr[index]
            next_unique += 1

    # Trim the array to contain only unique elements
    return arr[:next_unique]

test = [1, 2, 2, 3, 3, 4, 4, 4, 4]
print(remove_duplicates(test))

# O(N) TIME and SPACE