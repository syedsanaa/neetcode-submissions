class Solution:
    def insert(self, intervals, newInterval):
        res=[]
        for i in range(len(intervals)): 
            x,y=intervals[i]
            if y<newInterval[0]: 
                res.append([x,y])
            else: 
                res.append(newInterval) 
                while i<len(intervals): 
                    s,e=res[-1]
                    x,y=intervals[i]
                    if x<=e: 
                        res[-1]=[min(s,x),max(e,y)]
                    else: 
                        res.append(intervals[i])
                    i+=1 
                return res 
        res.append(newInterval)
        return res

