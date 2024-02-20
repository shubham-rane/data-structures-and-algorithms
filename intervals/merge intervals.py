class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        ans.append(intervals.pop(0))
        while intervals:
            new = intervals.pop(0)
            last = ans[-1]
            if new[0] <= last[1]:
                ans[-1][1] = max(new[1], last[1])
            else:
                ans.append(new)
        return ans
        
        