class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={0:0}
        for i in range(min(coins),amount+1): 
            res=float('inf')
            for j in coins: 
                if j<=i and i-j in dp: 
                    res=min(res,dp[i-j]+1)
            dp[i]=res
        if dp.get(amount, float('inf'))==float('inf'): 
            return -1 
        else: 
            return dp[amount]
