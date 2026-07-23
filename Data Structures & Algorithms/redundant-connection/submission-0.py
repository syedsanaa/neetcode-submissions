class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        degree=defaultdict(int) 
        for x,y in edges: 
            graph[x].append(y)
            graph[y].append(x)
            degree[x]+=1 
            degree[y]+=1 
        q=deque() # only put in nodes that will either have degree 1 or after doing dfs we make there degree 1 
        for k,v in degree.items(): 
            if v==1: 
                q.append(k)
        while q: 
            node=q.popleft()
            degree[node]-=1 
            for nei in graph[node]: 
                degree[nei]-=1 
                if degree[nei]==1: 
                    q.append(nei)
        for x,y in reversed(edges): 
            if degree[x]==2 and degree[y]!=0: 
                return [x,y] 
        return []
        