class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L=0
        leng=len(nums)
        maxlen=0
        for R in range(len(nums)): 
            if nums[R]==0: 
                k-= 1 
            while k<0  : 
                if nums[L]==0: 
                    k+=1 
                L+=1 
            maxlen=max(maxlen,R-L+1)
        return maxlen 
