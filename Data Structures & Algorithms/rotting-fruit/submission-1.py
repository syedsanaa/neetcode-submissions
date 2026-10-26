class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0 
        q=deque()
        l,m=len(grid),len(grid[0])
        for i in range(l): 
            for j in range(m): 
                if grid[i][j]==1:
                    fresh+=1 
                if grid[i][j]==2: 
                    q.append((i,j))
        time=0
        direct=[[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh>0:
            time+=1 
            for _ in range(len(q)): 
                x,y=q.popleft()
                for xi,yi in direct: 
                    if min(x+xi,y+yi)<0 or x+xi>=l or y+yi>=m or grid[x+xi][y+yi]!=1: 
                        continue 
                    fresh-=1 
                    grid[x+xi][y+yi]=2
                    q.append((x+xi,y+yi))
        return time if not fresh else -1 


