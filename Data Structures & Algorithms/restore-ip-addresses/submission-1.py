class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]: 
        if len(s)>12: 
            return []
        finalres=[]
        #dleft is the dots left before crnt itr dot is palced so start with 3 
        def dfs (i,dleft,res): 
            if i==len(s): 
                if dleft==-1:
                    finalres.append(res[0:-1])
                return 
            string=''
            if s[i]!='0':
                for j in range(i,min(i+3,len(s))):
                    string+=s[j]
                    if len(s)-j-1<=dleft*3 and int(string)<=255 and len(s)-j-1>=dleft :
                        dfs(j+1,dleft-1,res+string+'.')
            else: 
                dfs(i+1,dleft-1,res+s[i]+'.')
            return 
        dfs(0,3,'')
        return finalres