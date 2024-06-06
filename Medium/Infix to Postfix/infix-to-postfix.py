#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
    
    
            d={"+":1,"-":1,"*":2,"/":2,"^":3,"(":0}
            res=''
            st=[]
            
            for i in range(len(exp)):
                if exp[i]=="(":
                    st.append(exp[i])
    
    
                elif exp[i]==")":
                    while st[-1]!="(":
                        res=res+st.pop()
                    st.pop()
    
    
                elif exp[i] in d:
                    while st and d[st[-1]]>=d[exp[i]]:
                        res=res+st.pop()
                    st.append(exp[i])
    
    
                else:
                    res=res+exp[i]
                
            while st:
                res=res+st.pop()
            return res
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends