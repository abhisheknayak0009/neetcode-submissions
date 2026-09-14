class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # normally hashset would work but as we have to maintain index
        # hashmap would be better
        hashmap_nums = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if(difference in hashmap_nums):
                return [hashmap_nums[difference], i]
            hashmap_nums[nums[i]] = i
        return None