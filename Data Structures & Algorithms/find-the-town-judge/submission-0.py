class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Indegree=defaultdict(int)  # no of people trusting the key 
        Outdegree={}  #  value is all the people key trusts 
        for a,b in trust: 
            Indegree[b]+=1 
            Outdegree[a]=0
        for i in range(1,n+1): 
            if i not in Outdegree.keys() and Indegree[i]==n-1: 
                return i 
        return -1