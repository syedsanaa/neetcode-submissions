class Solution:
    def numSquares(self, n: int) -> int:
        dp={0:0}
        for i in range(1,n+1): 
            res=float('inf')
            for j in range(1,i+1): 
                if j**2>i: 
                    break 
                else: 
                    res=min(res,dp[i-j**2]+1)
            dp[i]=res 
        return dp[n]

        