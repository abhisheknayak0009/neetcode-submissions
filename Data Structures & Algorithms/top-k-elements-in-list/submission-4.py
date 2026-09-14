class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        top_k_elements = []
        
        if not nums or len(nums) == 0 or k > len(nums):
            return top_k_elements
        
        # creating buckets
        # it looks like this [[], [], [], []]
        buckets = [[] for i in range(len(nums) + 1)]
        count_nums = {}

        for i in range(len(nums)):
            count_nums[nums[i]] = count_nums.get(nums[i], 0) + 1
        
        for index, count in count_nums.items():
            buckets[count].append(index)
        
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                if k > 0:
                    top_k_elements.append(buckets[i][j])
                    k -= 1
                else:
                    return top_k_elements
        return top_k_elements