#User function Template for python3

class Solution:
    def canRepresentBST(self, arr, N):
        # code here
        stack = []
        root = float('-inf')
        for element in arr:
            if element < root:
                return 0
            while stack and element > stack[-1]:
                root = stack.pop()
            stack.append(element)
        return 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.canRepresentBST(arr, N))
# } Driver Code Ends