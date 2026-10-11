class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # make s and t ints 
        deadends=set(deadends)
        def bfs(s,t):
            if s==t: 
                return 0 
            if s in deadends: 
                return -1 
            q = deque([s])
            visited = {s}
            moves=0 
            while q: 
                moves+=1 
                for _ in range(len(q)): 
                    node=q.popleft()
                    for i in range(4): 
                        for j in [-1,1]:
                            temp=list(node) 
                            temp[i]=str((int(temp[i])+j)%10)
                            temp="".join(temp)
                            if temp==t:
                                return moves 
                            if temp not in visited and temp not in deadends : 
                                visited.add(temp)
                                q.append(temp) 
            return -1 
        return bfs('0000',target)
