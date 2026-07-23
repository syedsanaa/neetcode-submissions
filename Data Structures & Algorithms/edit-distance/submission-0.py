class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        maxj=len(word2)
        maxi=len(word1)
        def recursion(i,j,count): 
            if j>=maxj: 
                return count+maxi-i
            if i>=maxi: 
                return count+maxj-j
            if word1[i]==word2[j]: 
               return recursion(i+1,j+1,count)
            else:
                return min(recursion(i,j+1,count+1),
                recursion(i+1,j,count+1),
                recursion(i+1,j+1,count+1))
        return recursion(0,0,0)