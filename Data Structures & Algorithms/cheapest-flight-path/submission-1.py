class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float('inf') for _ in range(n)]
        prices[src]=0 
        for _ in range(k+1): 
            temp=prices.copy()
            for sr,ds,pr in flights: 
                if prices[sr]==float('inf'): 
                    continue 
                if prices[sr]+pr<temp[ds]: 
                    temp[ds]=prices[sr]+pr
            prices=temp 
        return prices[dst] if prices[dst]!=float('inf') else -1