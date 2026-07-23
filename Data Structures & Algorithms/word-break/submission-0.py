class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        DP={}

        def bactracking(i): 
            if i in DP: 
                return DP[i]
            if i==len(s):  
                return True 
            else: 
                for word in wordDict: 
                    start=i 
                    end=i+len(word)
                    if s[start:end]==word: 
                        if bactracking(end): 
                            DP[i]=True
                            return True  
                DP[i]=False
                return False  
        return bactracking(0)