#User function Template for pytho

from functools import cmp_to_key
class Solution:

    def printLargest(self, n, arr):
        # code here
        
        key =  lambda item1, item2: 1 if item1 + item2 > item2 + item1 else -1
        
        arr.sort(key =  cmp_to_key(key), reverse = True)
        
        #print(arr)
        
        return "".join(arr)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends