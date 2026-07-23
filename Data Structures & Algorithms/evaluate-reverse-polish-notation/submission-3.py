class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for nums in tokens: 
            if nums not in "+-*/": 
                stack.append(int(nums))
            else: 
                n2=stack.pop()
                n1=stack.pop()
                if nums=="*": 
                    stack.append(n1*n2)
                elif nums=="/": 
                    stack.append(int(n1 / n2))
                elif nums=="+": 
                    stack.append(n1+n2)
                elif nums=="-": 
                    stack.append(n1-n2)
        return stack[-1]