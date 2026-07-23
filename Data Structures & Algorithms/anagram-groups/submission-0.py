class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}
        for i in range(len(strs)): 
            List=[0]*26
            for ch in strs[i]:
                index=ord(ch) - ord('a')
                List[index]+=1
            List=tuple(List)
            if dicti.get(List,[0])!=[0] : 
                dicti[List].append(strs[i])
            else: 
                dicti[List]=[strs[i]]
        dicti = list(dicti.values())
        return dicti

                    
        
