class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # keep a hashset
        nums_hash = set()
        for n in nums:
            if n in nums_hash:
                return True
            nums_hash.add(n)
        return False