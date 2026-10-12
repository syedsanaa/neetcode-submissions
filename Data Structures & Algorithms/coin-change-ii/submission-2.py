class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        def dfs(amount,i): 
            if (amount,i) in cache: 
                return cache[(amount,i)]
            if amount==0: 
                return 1 
            res=0
            for j in range(i,len(coins)): 
                if amount-coins[j]>=0: 
                    res+=dfs(amount-coins[j],j)
            cache[(amount,i)]=res
            return res 
        return dfs(amount,0)