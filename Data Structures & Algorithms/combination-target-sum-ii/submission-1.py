class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        leng=len(candidates)
        res=[]
        def dfs(i,curr,total): 
            if total==target: 
                res.append(curr.copy())
                return 
            if i>=leng or total>target: 
                return  
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()
            while i<leng-1 and candidates[i]==candidates[i+1]: 
                i+=1 
            dfs(i+1,curr,total)
            return 
        dfs(0,[],0)
        return res

            


