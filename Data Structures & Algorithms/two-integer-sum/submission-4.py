class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                if i > hashmap[difference]:
                    return[hashmap[difference], i]
                else:
                    return[i, hashmap[difference]]
            hashmap[nums[i]] = i
        return None