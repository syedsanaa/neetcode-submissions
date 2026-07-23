class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adjlist=defaultdict(list)
        for x,y in edges: 
            adjlist[x].append(y)
            adjlist[y].append(x)
        lenlist={}
        leaves=deque()
        for k,v in adjlist.items(): 
            leng=len(v)
            if leng==1: 
                leaves.append(k)
            lenlist[k]=leng
        while leaves and len(adjlist)>2: 
            for i in range(len(leaves)): 
                node=leaves.popleft()
                child=adjlist[node][0]
                adjlist[child].remove(node)
                lenlist[child]-=1 
                if lenlist[child]==1: 
                    leaves.append(child)
                del adjlist[node] 
                del lenlist[node]
        return list(adjlist.keys())
                





        
            

        