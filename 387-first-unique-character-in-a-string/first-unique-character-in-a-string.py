class Solution:
    def firstUniqChar(self, s):
       
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for index, char in enumerate(s):
            if count[char] == 1:
                return index     
        return -1