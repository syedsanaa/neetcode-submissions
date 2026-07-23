class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd={}
        td={}
        for i in range(len(s)):
            if s[i] in sd and sd[s[i]]!=t[i]: 
                return False 
            if t[i] in td and td[t[i]]!=s[i]: 
                return False 
            sd[s[i]]=t[i]
            td[t[i]]=s[i]
        return True



        