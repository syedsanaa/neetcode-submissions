class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        maxx=len(grid)
        maxy=len(grid[0])
        direct=[[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(x,y): 
            if min(x,y)>= 0 and x<maxx and y<maxy and grid[x][y]==1:
                grid[x][y]=2  
                q.append((x,y,0))
                for i,j in direct:
                        dfs(x+i,y+j)
            return 
        q=deque()
        for x in range(maxx): 
            for y in range(maxy): 
                if grid[x][y]==1: 
                    dfs(x,y)
                    break  
            if q: 
                break 
        while q: 
            x,y,l=q.popleft()
            for i,j in direct: 
                nx=x+i 
                ny=y+j
                if min(nx,ny)>= 0 and nx<maxx and ny<maxy and grid[nx][ny]==1: 
                    return l
                if min(nx,ny)>= 0 and nx<maxx and ny<maxy and grid[nx][ny]==0:
                    grid[nx][ny]=2
                    q.append((nx,ny,l+1))
                