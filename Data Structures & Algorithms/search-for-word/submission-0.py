class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxi=len(board)
        maxj=len(board[0])
        path=set()
        def dfs(index,i,j): 
            if index==len(word): 
                return True 
            if i<0 or i>=maxi or j<0 or j>=maxj or word[index]!= board[i][j] or (i,j) in path : 
                return False 
            path.add((i,j))
            res=(dfs(index+1,i+1,j)or dfs(index+1,i-1,j) or dfs(index+1,i,j-1) or dfs(index+1,i,j+1))
            path.remove((i,j))  # FORGOT THIS 
            return res 

        for i in range(maxi): 
            for j in range(maxj): 
                if dfs(0,i,j): 
                    return True
        return False 