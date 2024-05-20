#User function Template for python3
import math
class Solution:
    def divide(self, a, b):
        sign=1
        if (a<0 and b>0) or (a>0 and b<0):
            sign=-1
        a=abs(a)
        b=abs(b)
        
        return (sign)*(a//b)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        ob=Solution()
        
        print(ob.divide(a,b))
        
# } Driver Code Ends