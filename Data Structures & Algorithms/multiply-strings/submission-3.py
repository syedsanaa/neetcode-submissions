class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        out=0 
        carry=0
        if len(num1)>len(num2): 
            num1,num2=num2,num1
        for i in range(len(num1)-1,-1,-1): 
            digit=10**(len(num1)-1-i) 
            for j in range(len(num2)-1,-1,-1):
                partsum=(10**(len(num2)-1-j))*digit
                mult=(int(num1[i])*int(num2[j])) + carry
                carry= mult//10 
                out+= ((mult%10)*partsum)
            out+=(carry*partsum*10)
            carry=0
        return str(out)
        