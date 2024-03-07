class Solution:
    def customSortString(self, order, s):
        # Count occurrences of characters in s
        counts = Counter(s)
        result = []

        # Append characters from s in the order specified by 'order'
        for char in order:
            if char in counts:
                result.append(char * counts[char])
                # Remove counted characters from counts
                del counts[char]

        # Append remaining characters in s
        for char, count in counts.items():
            result.append(char * count)

        return ''.join(result)