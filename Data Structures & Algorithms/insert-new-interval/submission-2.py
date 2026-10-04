class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        if not intervals or newInterval[0] <= intervals[0][0]:
            intervals.insert(0, newInterval)
        else:
            for i in range(len(intervals)): 
                if i!=len(intervals)-1 and intervals[i][0]<=newInterval[0]<=intervals[i+1][0]: 
                    intervals.insert(i+1,newInterval)
                    break
        if n==len(intervals): 
            intervals.append(newInterval)
        newres=[]
        i=0
        while i<len(intervals): 
            s=intervals[i][0]
            e=intervals[i][1]
            while i<len(intervals)-1 and s<=intervals[i+1][0]<=e: 
                e=max(e,intervals[i+1][1])
                i+=1
            newres.append([s,e])
            i+=1 
        return newres 
            