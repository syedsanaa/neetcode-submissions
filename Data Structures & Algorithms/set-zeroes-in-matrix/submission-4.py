class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row1=False 
        for i in range(len(matrix[0])): 
            if matrix[0][i]==0: 
                row1=True 
                break 
        for r in range(1,len(matrix)): 
            for c in range(len(matrix[0])): 
                if matrix[r][c]==0 : 
                    matrix[0][c]=0 
                    matrix[r][0]=0 
        for r in range(1,len(matrix)): 
            for c in range(len(matrix[0])-1,-1,-1): 
                if matrix[0][c]==0 or matrix[r][0]==0: 
                    matrix[r][c]=0

        if row1:
            for i in range(len(matrix[0])): 
                matrix[0][i]=0 
        
        