class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort() #ascending 
        res=0
        MOD = 10**9 + 7
        for l in range(len(nums)): 
            r=l 
            while r<len(nums) and nums[l]+nums[r]<=target: 
                res = (res + pow(2, max(0, r - l - 1), MOD)) % MOD
                r+=1 
        return res
