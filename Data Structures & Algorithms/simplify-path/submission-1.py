class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        l=len(path)
        s=''
        dcount=0
        for i in path: 
            if i=='/': 
                if s and s!='..' and s!='.':  
                    stack.append(s)
                elif s and s=='..' and stack: 
                    stack.pop()
                s=''
            else:
                s=''.join([s,i])
        if s and s!='..' and s!='.':  
            stack.append(s)
        elif s and s=='..' and stack: 
            stack.pop()
        return "/" + "/".join(stack)