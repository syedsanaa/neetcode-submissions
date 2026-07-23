class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        leng=len(nums)
        h=defaultdict(int)
        for i in nums: 
            h[i]+=1
        out=[]
        def dfs(i,perm): #perm is a list 
            if i==leng: 
                out.append(perm.copy()) 
                return 
            for k,v in h.items(): 
                if v>0: 
                    h[k]-=1 
                    perm.append(k)
                    dfs(i+1,perm)
                    perm.pop()
                    h[k]+=1 
            return 
        dfs(0,[])
        return out 
        
            

