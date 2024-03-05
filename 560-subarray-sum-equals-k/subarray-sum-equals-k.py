class Solution:
	def subarraySum(self, nums, k):

		result = prefixsum = 0
		hashmap = {0:1}

		for num in nums:
			prefixsum = prefixsum + num

			if prefixsum-k in hashmap:
				result += hashmap[prefixsum-k]

			if prefixsum not in hashmap:
				hashmap[prefixsum] = 1
                
			else:
				hashmap[prefixsum] = hashmap[prefixsum]+1

		return result
    
    # O(N) TIME and SPACE COMPLEXITY