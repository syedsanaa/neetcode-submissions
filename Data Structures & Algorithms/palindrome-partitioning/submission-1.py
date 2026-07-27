class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispallindrome(string): 
            r=len(string)-1 
            l=0
            while l<=r: 
                if string[l]!=string[r]: 
                    return False 
                r-=1 
                l+=1 
            return True 
        dp={}
        res=[]
        def dfs(i,temp): 
            if i==len(s): 
                res.append(temp)
                return 
            news=''
            for j in range(i,len(s)): 
                news+=s[j]
                if ispallindrome(news):
                    result=dfs(j+1, temp + [news])
            return 
        dfs(0,[])
        return res 