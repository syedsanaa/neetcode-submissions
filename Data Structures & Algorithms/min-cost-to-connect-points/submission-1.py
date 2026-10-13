
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjlist=defaultdict(list)
        for x,y in points: 
            for a,b in  points: 
                dist=abs(a - x) + abs(b - y)
                adjlist[(x,y)].append((dist,a,b))
        heap=[(0,points[0][0],points[0][1])]
        visit=set()
        cost=0 
        while heap: 
            d,x,y=heapq.heappop(heap)
            if (x,y) in visit: 
                continue 
            visit.add((x,y))
            cost+=d 
            for d1,x1,y1 in adjlist[(x,y)]: 
                if (x1,y1) not in visit: 
                    heapq.heappush(heap,(d1,x1,y1))
        return cost 