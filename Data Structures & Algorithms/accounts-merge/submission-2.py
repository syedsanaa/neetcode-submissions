class UninonFind: 
    def __init__(self,n): 
        self.par=[i for i in range(n)]
        self.rank=[1]*n 
    def find(self,node): 
        if self.par[node]!=node: 
            self.par[node]=self.find(self.par[node])
        return self.par[node]
    def union(self,n1,n2): 
        p1,p2=self.find(n1),self.find(n2)
        if p1==p2: 
            return 
        if self.rank[p1]>self.rank[p2]: 
            self.par[p2]=p1 
            self.rank[p1]+=self.rank[p2]
        else: 
            self.par[p1]=p2 
            self.rank[p2]+=self.rank[p1]
        return True 
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        etoacc={}
        uf=UninonFind(len(accounts))
        for i,acc in enumerate(accounts): 
            for e in acc[1:]: 
                if e in etoacc: 
                    uf.union(etoacc[e],i)
                else: 
                    etoacc[e]=i 
        acc=defaultdict(list)
        for k,v in etoacc.items(): 
            acc[uf.find(v)].append(k)
        res=[]
        for ind,e in acc.items(): 
            res.append([accounts[ind][0]]+sorted(e))
        return res

        
                    


