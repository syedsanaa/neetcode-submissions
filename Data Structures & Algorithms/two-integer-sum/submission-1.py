class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num={}
        for i in range(len(nums)): 
            if target-nums[i] in num: 
                return [num[target-nums[i]],i]
            num[nums[i]]=i
        