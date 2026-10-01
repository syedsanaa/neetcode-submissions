class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        for i in s: 
            if i==']' and stack: 
                stack.pop()
            else: 
                stack.append(i)
        return int(len(stack)/2)