class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd=defaultdict(int)
        td=defaultdict(int)
        for i in s: 
            sd[i]+=1 
        for i in t: 
            td[i]+=1 
        return True if sd==td else False 