class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for i in range(len(s)): 
            if stack and stack[-1][1]==k: 
                stack.pop()
            if stack and stack[-1][0]==s[i]: 
                stack[-1][1]+=1 
            else: 
                stack.append([s[i],1])
        if stack and stack[-1][1]==k: # FOR EDGE CASE I WASNT ABLE TO PREDICT 
                stack.pop()
        out=''
        while stack: 
            letter,no=stack.pop()
            out=''.join([letter*no,out])
        return out 
