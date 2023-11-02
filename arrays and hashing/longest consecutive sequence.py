class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        
        count = 0
        for start in numset:
            if start - 1 not in numset:
                end = start+1
                while end in numset:
                    end+=1
                count = max(count,end-start)
            
        return count

