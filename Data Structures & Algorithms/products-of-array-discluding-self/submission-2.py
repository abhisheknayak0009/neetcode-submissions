class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        for i in range(1, len(nums)):
            prod[i] = prod[i-1] * nums[i-1]
        
        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] = prefix * prod[i]
            prefix *= nums[i]
        return prod