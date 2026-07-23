class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r=len(matrix)
        c=len(matrix[0])
        dp={}
        def dfs(i,j): 
            if i==r or j==c or matrix[i][j]=='0': 
                return 0 
            if (i,j) in dp: 
                return dp[(i,j)]
            length=min(dfs(i+1,j),dfs(i,j+1),dfs(i+1,j+1))+1 
            dp[(i,j)]=length
            return length
        res=0 
        for i in range(r): 
            for j in range(c): 
                res=max(res,dfs(i,j))
        return res**2