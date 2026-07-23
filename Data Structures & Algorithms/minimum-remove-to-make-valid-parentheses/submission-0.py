from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res=deque()
        for i in range(len(s)): 
            if s[i]==")" and res and res[-1][0]=="(": 
                res.pop()
            elif not s[i].isalpha(): 
                res.append([s[i],i]) 
        res={row[1] for row in res}
        ret=''
        for i in range(len(s)): 
            if i not in res: 
                ret += s[i]
        return ret
    