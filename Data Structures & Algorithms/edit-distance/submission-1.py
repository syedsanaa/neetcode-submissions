class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        maxj=len(word2)
        maxi=len(word1)
        dp={}
        def recursion(i,j): 
            if (i,j) in dp:
                return dp[(i,j)]
            if j>=maxj: 
                return maxi-i
            if i>=maxi: 
                return maxj-j
            if word1[i]==word2[j]: 
               return recursion(i+1,j+1)
            else:
                res=min(recursion(i,j+1)+1,
                recursion(i+1,j)+1,
                recursion(i+1,j+1)+1)
                dp[(i,j)]=res
                return res
        return recursion(0,0)