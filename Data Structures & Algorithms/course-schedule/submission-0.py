class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for i in prerequisites: 
            graph[i[1]].append(i[0])
        visiting=defaultdict(int)
        # 0 not visited , 1 visiting , 2 visited 
        def dfs(node): 
            if graph[node]==[] or node not in graph: 
                return True 
            if visiting[node]==1: 
                return False 
            visiting[node]=1
            for child in graph[node]: 
                if not dfs(child): 
                    return False 
            visiting[node]=2
            graph[node]=[]
            return True
 
        
        for c in range(numCourses):
            if not dfs(c): 
                return False 
        return True 

