class Solution:
    def checkValidString(self, s: str) -> bool:
        "((**))))"
        stack=[]
        sstack=[]
        for i in range(len(s)): 
            if s[i]=="(": 
                stack.append(i) 
            elif s[i]=="*": 
                sstack.append(i) 
            else: 
                if stack: 
                    stack.pop()
                elif sstack: 
                    sstack.pop()
                else: 
                    return False 
        while stack: 
            if sstack and stack[-1]<sstack[-1]: 
                sstack.pop()
                stack.pop()
            else: 
                return False 
        return True 
                    