class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        curr = 0
        for i in range(0, len(nums)):
            curr += nums[i]
            if maxsum < curr:
                maxsum = curr
            if curr < 0:
                curr = 0
        return maxsum


        