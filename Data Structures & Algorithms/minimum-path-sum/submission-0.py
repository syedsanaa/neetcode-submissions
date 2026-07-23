class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)-1
        c=len(grid[0])-1
        dp={}
        def dfs(i,j): 
            if i==r and j==c: 
                return grid[i][j]
            if i>r or j>c: 
                return float('inf')
            if (i,j) in dp: 
                return dp[(i,j)]
            res=min(dfs(i+1,j),dfs(i,j+1))+grid[i][j]
            dp[(i,j)]=res
            return dp[(i,j)] 
        return dfs(0,0)