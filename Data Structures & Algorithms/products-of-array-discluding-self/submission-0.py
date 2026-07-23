class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng=len(nums)
        d=[[1,1] for i in range(leng)] 
        preifxm=1 
        suffixm=1 
        for i in range(leng):
            d[i][0]=preifxm
            d[leng-i-1][1]=suffixm
            preifxm*=nums[i]
            suffixm*=nums[leng-i-1]
        out=[]
        for i in range(leng): 
            out.append(d[i][0]*d[i][1])
        return out
        