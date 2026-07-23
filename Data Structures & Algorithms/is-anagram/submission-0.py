class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        List1=[0]*26
        List2=[0]*26
        for ch in s: 
            List1[ord(ch)-ord('a')]+=1
        for ch in t:
            List2[ord(ch)-ord('a')]+=1
        return List1==List2