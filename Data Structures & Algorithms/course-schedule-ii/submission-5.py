class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq=defaultdict(list)
        for x,y in prerequisites: 
            preq[x].append(y)
        
        output=[]
        visit,cycle=set(),set()

        def dfs(crs): 
            if crs in cycle: 
                return False 
            if crs in visit: 
                return True 
            cycle.add(crs)
            visit.add(crs)
            for pre in preq[crs]: 
                if not dfs(pre):
                    return False 
            cycle.remove(crs)
            output.append(crs)
            return True 
        for i in range(numCourses): 
            if not dfs(i): 
                return [] 
        return output
