class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_nums = set()
        for n in nums:
            if n in hash_nums:
                return True
            hash_nums.add(n)
        return False