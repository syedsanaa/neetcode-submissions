class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        endtime=[]
        res=0 
        for arival,wait in customers: 
            end=arival+wait
            if endtime and endtime[-1]>arival:
                res+=(endtime[-1]-arival) 
                end=endtime[-1]+wait
            res+=wait 
            endtime.append(end)
        return res/(len(customers))
