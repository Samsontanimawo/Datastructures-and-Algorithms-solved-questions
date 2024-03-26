class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        nums = list(freq.keys())
        k = len(nums)-k

        def quickSelect(left, right):
            pivot = nums[right]
            partition = left

            for index in range(left, right):
                if freq[nums[index]] <= freq[pivot]:
                    nums[index], nums[partition] = nums[partition], nums[index]
                    partition +=1

            nums[partition], nums[right] = nums[right], nums[partition]

            if partition < k:
                return quickSelect(partition + 1, right)

            elif partition > k:
                return quickSelect(left, partition - 1)

            else:
                nums[partition]

        quickSelect(0, len(nums)-1)

        return nums[k:]