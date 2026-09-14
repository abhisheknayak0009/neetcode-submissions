class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            currSum += nums[i]
            print("currSum", currSum)
            if currSum <= nums[i]:
                currSum = nums[i]
            maxVal = max(maxVal, currSum)
            print('maxval', maxVal)
        return maxVal