class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids: 
            if i<0: 
                while stack and stack[-1]>0: 
                    if stack[-1]==abs(i): 
                        i=0 
                        stack.pop()
                        break 
                    elif stack[-1]<abs(i): 
                        stack.pop()
                    elif stack[-1]>abs(i): 
                        i=0 
                        break 
            if i!=0: 
                stack.append(i)
        return stack 