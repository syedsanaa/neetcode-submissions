class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0 
        j=0 
        res=[]
        if not firstList or not secondList: 
            return []
        while j<len(secondList) and i<len(firstList): 
            #check if no intersection at all 
            if firstList[i][0]>secondList[j][1]: 
                j+=1  
                continue 
            if firstList[i][1]<secondList[j][0]: 
                i+=1 
                continue  
            # for start 
            start=max(firstList[i][0],secondList[j][0])
            # for end 
            if firstList[i][1]>secondList[j][1]: 
                end=secondList[j][1]
                j+=1 
            elif firstList[i][1]<secondList[j][1]:
                end=firstList[i][1]
                i+=1 
            else: 
                end=firstList[i][1]
                i+=1 
                j+=1 
            res.append([start,end])
        return res