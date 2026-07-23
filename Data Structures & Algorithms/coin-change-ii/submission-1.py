class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        leng=len(coins)
        dp={}
        def dfs(i,total): 
            if i>=leng or total>amount: 
                return 0 
            if total==amount: 
                return 1 
            if (i,total) in dp: 
                return dp[(i,total)]
            dp[(i,total)]= dfs(i,total+coins[i])+dfs(i+1,total) 
            return dp[(i,total)]
        return dfs(0,0)           