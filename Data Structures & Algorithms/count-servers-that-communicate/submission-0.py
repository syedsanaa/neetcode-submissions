class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowc=[0 for _ in range(len(grid))]
        colc=[0 for _ in range(len(grid[0]))]
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j]==1:
                    rowc[i]+=1 
                    colc[j]+=1 
        res=0
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (colc[j]>1 or rowc[i]>1): 
                    res+=1 
        return res 