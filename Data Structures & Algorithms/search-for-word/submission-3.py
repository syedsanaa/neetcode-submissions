class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        leng=len(word)
        maxx=len(board)
        maxy=len(board[0])
        # path=set() deifne later 
        def dfs(x,y,i):
            if x<0 or y<0 or x>=maxx or y>=maxy or (x,y) in path or board[x][y]!=word[i]: 
                return False 
            if i==leng-1: 
                return True
            path.add((x,y)) 
            res= (dfs(x+1,y,i+1) or dfs(x-1,y,i+1) or dfs(x,y+1,i+1)or dfs(x,y-1,i+1))
            path.remove((x,y))
            return res 

        for i in range(maxx): 
            for j in range(maxy):
                path=set()
                if dfs(i,j,0):
                    return True 
        return False 

