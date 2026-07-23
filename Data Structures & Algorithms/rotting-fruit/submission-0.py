class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxx=len(grid)
        maxy=len(grid[0])
        fresh=0
        q=deque() #popleft
        for x in range(maxx): 
            for y in range(maxy): 
                if grid[x][y]==1: 
                    fresh+=1 
                elif grid[x][y]==2: 
                    q.append([x,y])
        length=0    
        direct=[[-1,0],[1,0],[0,1],[0,-1]]
        while q and fresh>0: 
            for i in range(len(q)): 
                x,y=q.popleft()
                for xd,yd in direct: 
                    xn=x+xd
                    yn=y+yd 
                    if min(xn,yn)>=0 and xn<maxx and yn<maxy and grid[xn][yn]==1 : 
                        grid[xn][yn]=2
                        q.append([xn,yn])
                        fresh-=1 
            length+=1
        if fresh>0: 
            return -1 
        else: 
            return length 


        