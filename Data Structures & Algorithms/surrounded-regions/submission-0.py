class Solution:
    def solve(self, board: List[List[str]]) -> None:
        maxx=len(board)
        maxy=len(board[0])
        direct=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(root): # root=(x,y)
            x,y=root
            if board[x][y]!='#'and board[x][y]=='O' : 
                board[x][y]='#'
                for xd,yd in direct: 
                    xn=x+xd 
                    yn=y+yd
                    if min(xn,yn)>=0 and xn<maxx and yn<maxy and board[xn][yn]=='O': 
                        dfs((xn,yn))
            return
        for i in range(maxx): 
            dfs((i,0)) 
            dfs((i,maxy-1))
        for i in range(maxy): 
            dfs((0,i))
            dfs((maxx-1,i))
        for x in range(maxx): 
            for y in range(maxy): 
                if board[x][y]=='O': 
                     board[x][y]='X'
                elif  board[x][y]=='#': 
                     board[x][y]='O'
        