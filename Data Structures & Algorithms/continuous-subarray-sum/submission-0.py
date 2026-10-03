class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remain={0:-1}
        curr=0
        for i in range(len(nums)): 
            curr+=nums[i]
            r=curr%k 
            if r in remain and i-remain[r]>=2: 
                return True 
            elif r not in remain: 
                remain[r]=i
        return False 