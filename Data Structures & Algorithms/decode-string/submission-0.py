class Solution:
    def decodeString(self, s: str) -> str:
        #key idea: maintain an index i that loops through the entire 
        #string and adds each element in the stack , as soon as you 
        #encounter a closing bracket you wil start popping from the 
        #stack till you find a closing bracket and store all of that 
        # in a string after that you will continue popping from the stack 
        # till you are getting an isdigit and create a numebr from that 
        #and multiply to the str and add the final result to the stack and 
        #continue with the index i 
        i=0 
        leng=len(s)
        st=deque()
        while i<leng: 
            if s[i]==']': 
                element=st.pop()
                string=''
                while element!='[': 
                    string=''.join([element, string]) # can easily swap elements to swap order 
                    element=st.pop()
                num=''
                while st and st[-1].isdigit(): # stack was being empty 
                    num=st.pop()+num
                num=int(num)
                st.append(string*num)
            else : 
                st.append(s[i])
            i+=1
        return ''.join(st)


