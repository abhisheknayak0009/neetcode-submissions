class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        final = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for i in count:
            heapq.heappush(heap, [-1 * count[i], i])

        for i in range(k):
            count, digit = heapq.heappop(heap)
            final.append(digit)
        
        return final