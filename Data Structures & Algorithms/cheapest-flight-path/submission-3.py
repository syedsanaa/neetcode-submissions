class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist=[float('inf')]*n 
        dist[src]=0 
        stops=0 
        while stops<k+1: 
            temp=dist.copy()
            for x,y,p in flights: 
                if dist[x]+p<temp[y]: 
                    temp[y]=dist[x]+p
            dist=temp 
            stops+=1 
        return dist[dst] if dist[dst]!=float('inf') else -1

