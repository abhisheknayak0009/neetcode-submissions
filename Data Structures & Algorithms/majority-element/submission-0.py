class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_nums = {}
        for i in range(len(nums)):
            hash_nums[nums[i]] = hash_nums.get(nums[i],0) + 1
        
        for key in hash_nums:
            if hash_nums[key] >= (len(nums) // 2):
                return key
        return -1