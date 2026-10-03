class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1: 
            return -1 
        n=len(grid)
        q=deque([(0,0)])
        d=[[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        visited=set()
        visited.add((0,0))
        depth=0
        while q: 
            depth+=1
            for _ in range(len(q)):
                x,y=q.popleft()
                if (x,y)==(n-1,n-1): 
                    return depth
                for i,j in d: 
                    xn,yn=x+i,y+j 
                    if xn>=0 and xn<n and yn>=0 and yn<n and (xn,yn) not in visited and grid[xn][yn]==0: 
                        q.append((xn,yn))
                        visited.add((xn,yn))
        return -1

                


