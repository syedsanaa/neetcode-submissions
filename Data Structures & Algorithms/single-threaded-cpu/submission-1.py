class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorttask=[]
        for i in range(len(tasks)): 
            sorttask.append([tasks[i][0],tasks[i][1],i])
        sorttask=sorted(sorttask,key=lambda x:x[0])
        time=sorttask[0][0]
        h=[]
        s=0
        out=[]
        while len(out)!=len(sorttask): 
            i=0 
            while s+i<len(sorttask)and sorttask[s+i][0]<=time: 
                heapq.heappush(h,[sorttask[s+i][1],sorttask[s+i][0],sorttask[s+i][2]])
                i+=1 
            s=s+i 
            if h:
                duration,ava,task=heapq.heappop(h)
                out.append(task)
                time+=duration 
            else: 
                time=sorttask[s][0] 
        return out 
        