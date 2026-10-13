
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=set(nums)
        res=0 
        for i in nums: 
            if i-1 not in count: 
                temp=0
                j=i
                while j in count: 
                    temp+=1 
                    j+=1

                res=max(res,temp)
        return res 
