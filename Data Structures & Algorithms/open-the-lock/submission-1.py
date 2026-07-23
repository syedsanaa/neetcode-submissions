class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q=deque()
        q.append(([0,0,0,0],0))
        deadend = set(deadends)  
        visited = set() 
        visited.add("0000")
        if "0000" in deadends: 
            return -1 
        while q: 
            state,depth=q.popleft()
            state_str = ''.join(str(i) for i in state) 
            if state_str==target: 
                return depth
            for i in range(4):
                temp=state[i]

                #turn up 
                state[i]=(temp-1)%10 
                newstate_str=''.join(str(x) for x in state)
                if newstate_str not in deadend and newstate_str not in visited: 
                    q.append((state.copy(),depth+1))
                    visited.add(newstate_str)
                
                #turn down 
                state[i]=(temp+1)%10 
                newstate_str=''.join(str(x) for x in state)
                if newstate_str not in deadend and newstate_str not in visited: 
                    q.append((state.copy(),depth+1))
                    visited.add(newstate_str)

                state[i] = temp
        return -1 
            
