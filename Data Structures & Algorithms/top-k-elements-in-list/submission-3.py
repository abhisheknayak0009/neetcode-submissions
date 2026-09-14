class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        top_k_elements = []

        # edge cases
        if not nums or len(nums) == 0 or len(nums) < k:
            return top_k_elements

        count_nums = {}

        for i in range(len(nums)):
            count_nums[nums[i]] = 1 + count_nums.get(nums[i], 0)
        # now count_nums will have all the count values
        
        maxHeap = []
        for index, count in count_nums.items():
            heapq.heappush(maxHeap, [-1 * count, index])
        
        # now we will have values like [-3, 3], [-2, 2]
        while k > 0:
            count, index = heapq.heappop(maxHeap)
            top_k_elements.append(index)
            k -= 1
        
        return top_k_elements