class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        leng=len(nums)
        if not nums: 
            return 0 
        if leng==1: 
            return 1 
        
        Subs=[]
        def backtracking(index,nums,length,j):
            if index>=leng:
                Subs.append(length)
                return 
            else: 
                if j==-1 or nums[j]<nums[index] :
                    backtracking(index+1,nums,length+1,index)
                backtracking(index+1,nums,length,j)
        backtracking(0,nums,0,-1) 
        return max(Subs)
