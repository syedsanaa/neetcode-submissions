class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap=[(0,0,0)]
        visited=set() 
        direct=[[1,0],[-1,0],[0,1],[0,-1]]
        while heap: 
            w,x,y=heapq.heappop(heap)
            if (x,y) in visited: 
                continue 
            visited.add((x,y))
            if x==len(heights)-1 and y==len(heights[0])-1: 
                return w
            for i,j in direct: 
               xn,yn=x+i,y+j
               if min(xn,yn)>=0 and xn<len(heights) and yn<len(heights[0]) and (xn,yn) not in visited: 
                w1=max(w,abs(heights[x][y]-heights[xn][yn]))
                heapq.heappush(heap,(w1,xn,yn))
        return 0 
