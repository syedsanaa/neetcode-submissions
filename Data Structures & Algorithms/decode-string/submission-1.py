class Solution:
    def decodeString(self, s: str) -> str:
        count=[]
        string=[]
        cur=''
        k=0
        for i in s: 
            if i.isdigit(): 
                k=k*10 + int(i)
            elif i=='[': 
                count.append(k)
                string.append(cur)
                k,cur=0,''
            elif i==']':
                temp=cur 
                cur=string.pop()+temp*count.pop()
            else: 
                cur+=i 
        return cur 
            
