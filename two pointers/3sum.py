class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            start = i + 1
            end = len(nums) - 1
            
            while start <  end:
                s = nums[i] + nums[start] + nums[end]
                if s > 0:
                    end -= 1
                    
                elif s < 0:
                    start += 1
                    
                else:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        return ans
        