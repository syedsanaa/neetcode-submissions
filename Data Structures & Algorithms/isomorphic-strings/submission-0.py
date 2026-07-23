class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd=defaultdict(list)
        td=defaultdict(list) 
        for i in range(len(s)): 
            sd[s[i]].append(i)
            td[t[i]].append(i)
        for values in sd.values(): 
            if values not in td.values(): 
                return False 
        return True 


        