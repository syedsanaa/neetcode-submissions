class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l=r=0 
        if len(arr)==1: 
            return 1 
        a=True 
        b=True  
        res=0
        while r<len(arr)-1: 
            if a and arr[r]>arr[r+1]: 
                a=False
                b=True 
                #increase length 
                r+=1 
            elif b and arr[r]<arr[r+1]: 
                a=True
                b=False 
                r+=1 
            elif arr[r]==arr[r+1]:  
                r=l=r+1 
                a=b=True 
            else: 
                l=r 
                a=b=True 
            res=max(res,r-l+1)
        return res