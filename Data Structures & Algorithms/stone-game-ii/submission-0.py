class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp={}
        def dfs(alice,i,m): 
            if (alice,i,m) in dp: 
                return dp[(alice,i,m)]
            if i>=len(piles):
                return 0 
            maxscore=0
            res=0 if alice else float("inf")
            maxrang=min(len(piles),i+(2*m))
            for j in range(i,maxrang): 
                maxscore+=piles[j]
                if alice: 
                    res=max(res,dfs(not alice,j+1,max(m,j-i+1))+maxscore) 
                else: 
                    res=min(res,dfs(not alice,j+1,max(m,j-i+1))) 
            dp[(alice,i,m)]=res
            return res
        return dfs(True,0,1)