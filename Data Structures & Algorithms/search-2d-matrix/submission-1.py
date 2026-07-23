class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0 
        x=len(matrix)
        y=len(matrix[0])
        if x==1 and y==1 and matrix[0][0]==target: 
            return True 
        r=x*y-1
        while l<r: 
            m=(l+r)//2 
            if matrix[m//y][m%y]==target or matrix[l//y][l%y]==target or matrix[r//y][r%y]==target: 
                return True 
            elif matrix[m//y][m%y]>target: 
                r=m-1 
            elif matrix[m//y][m%y]<target:
                l=m+1 
        return False 
        