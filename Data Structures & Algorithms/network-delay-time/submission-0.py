class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist=defaultdict(list)
        for x,y,w in times: 
            adjlist[x].append((w,y))
        heap=[(0,k)]
        visit=set()
        res=0
        while heap: 
            w,i=heapq.heappop(heap)
            if i in visit: 
                continue 
            visit.add(i)
            res=max(res,w)
            for w1,i1 in adjlist[i]: 
                if i1 not in visit: 
                    heapq.heappush(heap,(w+w1,i1))
        return -1 if len(visit)<n else res
            
