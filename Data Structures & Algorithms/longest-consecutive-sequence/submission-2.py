class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCount = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in numsSet:
                length = 1
                while nums[i] + length in numsSet:
                    length += 1
                maxCount = max(maxCount, length)
        return maxCount