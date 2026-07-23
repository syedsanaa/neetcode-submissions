class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]: 
        nums.sort()
        out=[]
        leng=len(nums)
        def backtracking(i,curr): 
            if i>=leng: 
                out.append(curr.copy())
                return
            curr.append(nums[i])
            backtracking(i+1,curr) 
            curr.pop()
            while i<leng-1 and nums[i]==nums[i+1]: 
                i+=1 
            backtracking(i+1,curr)
        backtracking(0,[])
        return out 