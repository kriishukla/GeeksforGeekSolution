#User function Template for python3

class Solution:
    def maxAND(self, arr, n):
        ans = 0
        for j in range(20, -1, -1):
            p = 0
            prev = ans + (1 << j)
            
            for i in range(n):
                if (arr[i] & prev) == prev:
                    p += 1
            if p >= 2:
                ans += (1 << j)
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