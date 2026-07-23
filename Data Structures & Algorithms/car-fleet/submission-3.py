class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair={}
        for i in range(len(position)): 
            pair[position[i]]=speed[i]
        pair=dict(sorted(pair.items()))
        stack=[]
        stack.append(0)
        for dist,speed in pair.items():
            res= (target-dist)/speed
            # if prev ones have time less than equal to me 
            while stack and stack[-1] <= res: 
                stack.pop()
            stack.append(res)
        return len(stack )