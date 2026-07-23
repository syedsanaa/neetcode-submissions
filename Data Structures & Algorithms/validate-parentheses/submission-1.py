class Solution:
    def isValid(self, s: str) -> bool:
        i=0 
        leng=len(s)
        st=deque()
        d={']':'[','}':'{',")":'('}
        while i<leng:
            if s[i] in d:
                if not st or s[st.pop()]!=d[s[i]]: 
                    return False 
            else: 
                st.append(i)
            i+=1
        
        return True if not st else False 
