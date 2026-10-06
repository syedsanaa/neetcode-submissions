class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjlist=defaultdict(list)
        for i in range(len(points)): 
            xi,xj=points[i]
            for j in range(len(points)):
                yi,yj=points[j] 
                if i!=j: 
                    dist=abs(xi-yi)+abs(xj-yj)
                    adjlist[(xi,xj)].append([dist,yi,yj])
        heap=[(0,points[0][0],points[0][1])]
        visit=set()
        cost=0
        while heap: 
            d,x,y=heapq.heappop(heap)
            if (x,y) in visit: 
                continue 
            cost+=d 
            visit.add((x,y))
            for d1,x1,y1 in adjlist[(x,y)]: 
                if (x1,y1) not in visit: 
                    heapq.heappush(heap,(d1,x1,y1))

        return cost 