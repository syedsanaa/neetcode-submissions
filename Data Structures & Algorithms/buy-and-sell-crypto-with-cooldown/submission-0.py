class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leng=len(prices)
        dp={}
        def backtracking(i,buying): 
            if i>=leng:  
                return 0  
            if (i,buying) in dp:
                return dp[(i,buying)]
            donothing=backtracking(i+1,buying)
            if buying: 
                 res=max(donothing,backtracking(i+1,not buying)-prices[i])
            else: 
                res=max(donothing,backtracking(i+2,not buying)+prices[i])
            dp[(i,buying)]=res
            return res
        return backtracking(0,True)