#User function Template for python3
class Solution:

    def findMaximum(self,arr, n):
        for i in range(1,n):
            if arr[i]<=arr[i-1]:
                return arr[i-1]
            elif i==n-1:
                return arr[i]





#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends