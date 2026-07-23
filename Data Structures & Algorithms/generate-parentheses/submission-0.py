class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out=[]
        def backtracking(res,openS,closeS): 
            if openS+closeS==2*n: 
                out.append(''.join(res.copy()))
                return 
            if openS==closeS and openS<n:
                res.append('(')
                backtracking(res,openS+1,closeS)
                res.pop()
            elif openS<n:
                res.append('(')
                backtracking(res,openS+1,closeS)
                res.pop()
            if closeS<n and openS!=closeS: 
                res.append(')')
                backtracking(res,openS,closeS+1)
                res.pop()

        backtracking([],0,0)
        return out

