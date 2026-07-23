class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        out=[0 for i in temperatures]
        for i in range(len(temperatures)):
            j=1 
            while stack and temperatures[stack[-1]]<temperatures[i]:
                index=stack.pop()
                out[index]=i-index
            stack.append(i)
        return out 
