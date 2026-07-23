class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: 
            return True
        n=defaultdict(list)
        for i,j in edges: 
            n[i].append(j) 
            n[j].append(i)
        visiting=set()
        def dfs(node,par): 
            if node in visiting: 
                return False 
            if n[node]==[]: 
                return True 
            visiting.add(node)
            for c in n[node]:  
                if c == par:
                    continue
                if not dfs(c,node): 
                    return False 
            n[node]=[]
            visiting.remove(node)

            return True
        return dfs(edges[0][0],-1) and all(value == [] for value in n.values())
        


