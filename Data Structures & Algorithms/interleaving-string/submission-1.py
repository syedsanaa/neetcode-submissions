class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        if l1+l2!=l3: 
            return False
        dp={}
        def backtracking(i,j,k):
            if (i,j) in dp: 
                return dp[(i,j)]
            if k==l3: 
                return True 
            a=b=False 
            if j<l2 and s3[k]==s2[j]: 
                a=backtracking(i,j+1,k+1)
            if i<l1 and s3[k]==s1[i]: 
                b=backtracking(i+1,j,k+1)
            dp[(i,j)]=(a or b) 
            return (a or b) 
        return backtracking(0,0,0)