class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjlist=defaultdict(list)
        for i in range(len(isConnected)): 
            for j in range(len(isConnected)): 
                if isConnected[i][j]: 
                    adjlist[i].append(j)
                    adjlist[j].append(i)
        visited=set()
        def dfs(root):  
            nonlocal visited 
            for child in adjlist[root]: 
                if child not in visited: 
                    visited.add(child)
                    dfs(child)
            return 
        res=0 
        for keys in adjlist.keys(): 
            if keys not in visited: 
                visited.add(keys)
                dfs(keys)
                res+=1 
        return res 