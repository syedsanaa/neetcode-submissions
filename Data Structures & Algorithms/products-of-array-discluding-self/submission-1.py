class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1 for i in range(len(nums))]
        suff=[1 for i in range(len(nums))]
        prefp,suffp=1,1
        for i in range(len(nums)): 
            pref[i]=prefp
            suff[len(nums)-i-1]=suffp
            prefp*=nums[i]
            suffp*=nums[len(nums)-i-1]
        out=[]
        for i in range(len(nums)): 
            out.append(pref[i]*suff[i])
        return out