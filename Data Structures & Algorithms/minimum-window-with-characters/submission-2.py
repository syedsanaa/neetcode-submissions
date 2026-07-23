class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): 
            return ''
        want=defaultdict(int)
        for i in t: 
            want[i]+=1
        have=defaultdict(int)
        wantn=len(want)
        haven=0 
        l=0
        minlen=float('inf')
        minl=0
        minr=0
        for r in range(len(s)): 
            have[s[r]]+=1 
            if s[r] in want and have[s[r]]==want[s[r]]:  
                haven+=1  
            while haven==wantn: 
                if minlen>r-l+1:
                    minlen=r-l+1 
                    minl=l 
                    minr=r 
                have[s[l]]-=1 
                if have[s[l]]<want[s[l]]:  # I INITIALLIY PUT UNEQUAL 
                    haven-=1 
                l+=1 
        return s[minl:minr+1] if minlen!=float('inf') else ''

                

