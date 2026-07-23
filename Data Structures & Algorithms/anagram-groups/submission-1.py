class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D=defaultdict(list)
        for st in strs:
            List=[0]*26 
            for i in st: 
                index=ord(i) - ord('a') 
                List[index]+=1 
            D[tuple(List)].append(st)
        return list(D.values())

                    
        
