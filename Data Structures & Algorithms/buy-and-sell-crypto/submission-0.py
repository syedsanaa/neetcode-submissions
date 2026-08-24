class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0 
        sell=prices[len(prices)-1]
        for i in range(len(prices)-2,-1,-1): 
            sell=max(sell,prices[i+1])
            res=max(res,sell-prices[i])
        return res