class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for i in range(len(points)): 
            x,y=points[i] 
            d=(math.sqrt((0 - x)**2 + (0 - y)**2))
            heapq.heappush(h,(-d,i,points[i]))
            if len(h)>k: 
                heapq.heappop(h)
        return [c for a,b,c in h]