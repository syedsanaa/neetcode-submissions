class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rskip=0 
        dskip=0 
        while len(set(senate))>1: 
            res=[]
            for i in range(len(senate)): 
                if senate[i]=='R'and rskip==0: 
                    dskip+=1 
                    res.append('R')
                elif senate[i]=='R': 
                    rskip-=1 
                if senate[i]=='D'and dskip==0: 
                    rskip+=1 
                    res.append('D')
                elif senate[i]=='D': 
                    dskip-=1 
            senate=res
        if 'R' in set(senate): 
            return "Radiant"
        else: 
            return "Dire"
