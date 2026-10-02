class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        visited=set()
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j]==0: 
                    q.append((i,j))
                    visited.add((i,j))
        depth=0
        direct=[[1,0],[-1,0],[0,1],[0,-1]]
        while q: 
            depth+=1 
            for _ in range(len(q)): 
                x,y=q.popleft()
                for xn,yn in direct: 
                    if xn+x>=0 and xn+x<len(grid) and yn+y>=0 and yn+y<len(grid[0]) and grid[xn+x][yn+y]==(2**31)-1 and (xn+x,yn+y) not in visited: 
                        q.append((xn+x,yn+y))
                        grid[xn+x][yn+y]=depth 
                        visited.add((xn+x,yn+y))
        

        
