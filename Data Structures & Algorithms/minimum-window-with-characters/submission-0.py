class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq=defaultdict(int)
        for i in t: 
            freq[i]+=1
        dummy=defaultdict(int)
        have=0 
        need=len(freq)
        l=0
        minlen=10000000 
        result="" 
        for r in range(len(s)):
            dummy[s[r]]+=1
            if s[r] in freq and dummy[s[r]]==freq[s[r]]: 
                have+=1
                
                while have==need: 
                    if minlen>r-l+1: 
                        minlen=r-l+1 
                        result=s[l:r+1]
                    dummy[s[l]]-=1
                    if s[l] in freq and dummy[s[l]]<freq[s[l]]:
                        have-=1
                    l+=1
        return result

