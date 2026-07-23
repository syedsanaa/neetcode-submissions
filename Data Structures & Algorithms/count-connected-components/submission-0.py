class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g=defaultdict(list)
        for i in edges: 
            x,y=i 
            g[x].append(y)
            g[y].append(x)
        visited=set()
        def dfs(root,par): # root is just one node  
            visited.add(root)
            for child in g[root]:
                if child!=par and child not in visited:
                    dfs(child,root)
        out=0 
        for i in range(n): 
            if i not in visited: 
                dfs(i,float('inf'))
                out+=1 
        return out 