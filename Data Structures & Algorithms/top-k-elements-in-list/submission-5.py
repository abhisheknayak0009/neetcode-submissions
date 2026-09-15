class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_list = [[] for i in range(len(nums) + 1)]
        output = []
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        
        # remember hashmap.items() to iterate over key and value
        for key,value in hashmap.items():
            bucket_list[value].append(key)
        
        for i in range(len(nums), -1, -1):
            for j in range(len(bucket_list[i])):
                output.append(bucket_list[i][j])
                k -= 1
                if(k == 0):
                    return output
        return output