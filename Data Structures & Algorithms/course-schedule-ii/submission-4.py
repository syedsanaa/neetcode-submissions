class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        i=defaultdict(list)
        for a,b in prerequisites: 
            g[a].append(b)     # STORING PRE REQS OF A COURSE 
        visited=defaultdict(int)
        order=[]
        def dfs(root): 
            if visited[root]==-1: 
                return False 
            if visited[root]==1: 
                return True 
            visited[root]=-1
            for child in g[root]: 
                if  not dfs(child): 
                    return False 
            visited[root]=1
            order.append(root) 
            return True 
        for i in range(numCourses): 
            if visited[i]==0: 
               if not dfs(i): 
                    return [] 
        return order