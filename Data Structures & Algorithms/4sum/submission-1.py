class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        length=len(nums)
        nums.sort()
        def dfs(i,arr,total): 
            if len(arr)==4 and total==target: 
                res.append(arr.copy())
                return 
            if len(arr)>4 or i>=length: 
                return 
            arr.append(nums[i])
            dfs(i+1,arr,total+nums[i])
            arr.pop()
            temp=nums[i]
            while i<length and nums[i]==temp: 
                i+=1 
            dfs(i,arr,total)
            return 
        dfs(0,[],0)
        return res 