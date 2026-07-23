class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx=len(grid)
        maxy=len(grid[0])
        visited=set()
        def dfs(root): # root is (x,y)
            x,y = root 
            if min(x,y)<0 or x>=maxx or y>=maxy or grid[x][y]!=1 or root in visited : 
                return 0
            visited.add((x,y))
            return 1+dfs((x+1,y))+dfs((x-1,y))+dfs((x,y+1))+dfs((x,y-1))
        maxa=0
        for x in range(maxx): 
            for y in range(maxy): 
                if (x,y) not in visited: 
                    maxa=max(dfs((x,y)),maxa)
        return maxa