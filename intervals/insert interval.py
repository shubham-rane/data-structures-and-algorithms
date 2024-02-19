class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        ans = []

        #add all the non overlapping intervals smaller than the new interval
        i = 0 
        while i < len(intervals) and new_start > intervals[i][1]:
            ans.append(intervals[i])
            i += 1
        
        #merge overlapping intervals
        while i < len(intervals) and new_end >= intervals[i][0]:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        ans.append([new_start, new_end])
        return ans + intervals[i:]