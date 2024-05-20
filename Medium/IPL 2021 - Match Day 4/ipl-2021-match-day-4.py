#User function Template for python3

class Solution:
    #Complete this function
    # Function for finding maximum AND value.
    def maxAND(self, arr,n):
        x=0
        ans=0
        for i in range(17,-1,-1):
            c=0 
            for j in range(n):
                if (x&arr[j])==x and arr[j]&(1<<i):#check for  same previous pattern and  ith bit is set.
                    c+=1
                if c>=2:
                    break 
            if c>=2:
                ans+=1<<i 
                x+=1<<i  #setting the pattern for checking in  next iteration
        return ans 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxAND(arr,n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends