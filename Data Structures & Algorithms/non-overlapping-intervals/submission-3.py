class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prevend= intervals[0][1]
        out=0
        for i in range(1,len(intervals)): 
            if intervals[i][0]<prevend :
                out+=1
                prevend=min(intervals[i][1],prevend)
            else: 
                prevend=intervals[i][1]
        return out 