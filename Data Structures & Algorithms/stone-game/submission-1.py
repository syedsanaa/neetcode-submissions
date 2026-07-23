class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        player=True 
        total=sum(piles)
        dp={}
        def backtrack(i,j,player): 
            if i==j: 
                return 0 
            if (i,j,player) in dp: 
                return dp[(i,j,player)]
            if player: 
                res= max(backtrack(i+1,j,not player )+piles[i],backtrack(i,j-1,not player)+piles[j])
            else: 
                res= min(backtrack(i+1,j,not player),backtrack(i,j-1,not player))
            dp[(i,j,player)]=res 
            return res 
        score=backtrack(0,len(piles)-1,True)
        if score>total//2: 
            return True 
        else: 
            False 
