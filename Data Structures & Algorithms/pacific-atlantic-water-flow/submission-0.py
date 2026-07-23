class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #node is a list of height=x and lenfth=y coordinate 
        direct=[[1,0],[-1,0],[0,-1],[0,1]] #up down left right 
        maxx=len(heights)
        maxy=len(heights[0])
        def dfs(node,visited): 
            i,j=node 
            visited.add((i,j))
            for ni,nj in direct: 
                x,y=i+ni,j+nj 
                if 0<=x and x<maxx and 0<=y and y<maxy and heights[i][j]<=heights[x][y] and (x,y) not in visited: 
                    dfs([x,y],visited)
            return 
        Pacific=set()
        Atlantic=set()
        
        for i in range(maxy): 
            dfs([0,i],Pacific)
            dfs([maxx-1,i],Atlantic)
        for x in range(maxx): 
            dfs([x,0],Pacific)
            dfs([x,maxy-1],Atlantic)
        return [list(coord) for coord in (Pacific & Atlantic)]


