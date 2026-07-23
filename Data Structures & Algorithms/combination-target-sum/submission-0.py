class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out=[]
        maxl=len(nums)
        def backtracking(i,curr,total):
            if total== target: 
                out.append(curr.copy())
                return
            if i>= maxl: 
                return 
            if total>target: 
                return  
            curr.append(nums[i])
            backtracking(i,curr,total+nums[i])
            curr.pop()
            backtracking(i+1,curr,total)
            return 
        backtracking(0,[],0)
        return out 