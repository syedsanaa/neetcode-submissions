class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if m==1 and n==1: 
            return 0 if obstacleGrid[0][0]==1 else 1
        dp={}
        def backtrack(i,j): 
            if i==m-1 and j==n-1: 
                return 1
            if i>=m or j>=n or obstacleGrid[i][j]==1: 
                return 0 
            if (i,j) in dp: 
                return dp[(i,j)]
            dp[(i,j)]=backtrack(i+1,j)+backtrack(i,j+1)
            return dp[(i,j)]
        return backtrack(0,0)   