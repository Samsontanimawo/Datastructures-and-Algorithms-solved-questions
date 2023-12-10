class Solution(object):
    def topKFrequent(self, words, k):
        word_count = Counter(words)

        heap = [(-freq, word) for word, freq in word_count.items()]
        heapq.heapify(heap)

        result = [heapq.heappop(heap)[1] for _ in range(k)]

        return result