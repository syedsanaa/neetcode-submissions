from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1d = defaultdict(int)
        for i in s1:
            s1d[i] += 1
        
        have = defaultdict(int)
        s1l = len(s1)
        l = 0
        
        for r in range(len(s2)):
            have[s2[r]] += 1
            
            if r - l + 1 == s1l:
                if have == s1d:
                    return True
                else:
                    have[s2[l]] -= 1
                    if have[s2[l]] == 0:
                        del have[s2[l]]
                    l += 1
                    
        return False


        
        