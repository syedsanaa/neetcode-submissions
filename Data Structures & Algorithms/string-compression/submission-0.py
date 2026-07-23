class Solution:
    def compress(self, chars: List[str]) -> int:
        l=r=0
        leng=0
        llen=len(chars)
        while r<llen: 
            temp=chars[r]
            leng+=1
            count=0
            while r<llen and chars[r]==temp : 
                count+=1
                r+=1 
            if count>1 and count<10: 
                leng+=1 
                chars[l]=temp 
                chars[l+1]=str(count)
                l+=2 
            elif count>1 and count>=10: 
                leng+=len(str(count))
                chars[l]=temp 
                l+=1 
                for i in str(count): 
                    chars[l]=i 
                    l+=1 
            elif count==1: 
                chars[l]= temp 
                l+=1 
        return leng


