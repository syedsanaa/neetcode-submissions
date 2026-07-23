class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        leng=len(nums)
        nums.sort()
        prev=float('-inf')
        out=[]
        for i,a in enumerate(nums): 
            s=-a
            if i>0 and a==nums[i-1]: 
                continue 
            l=i+1 
            r=leng-1 
            while l<r:
                if nums[r]+nums[l]>s: 
                    r-=1 
                elif nums[r]+nums[l]<s: 
                    l+=1 
                else: 
                    out.append([-s,nums[r],nums[l]])
                    l+=1 
                    r-=1 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return out 


        