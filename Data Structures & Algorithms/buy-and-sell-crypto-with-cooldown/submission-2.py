class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache={}
        def dfs(i,s): 
            if (i,s) in cache: 
                return cache[(i,s)]
            if i>=len(prices): 
                return 0 
            res=0 
            if s>=0: 
                res=max(dfs(i+2,-1)+prices[i]-prices[s],dfs(i+1,s))
            else: 
                res=max(dfs(i+1,i),dfs(i+1,-1)) 
            cache[(i,s)]=res
            return res 
        return dfs(0,-1)