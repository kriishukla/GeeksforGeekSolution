#User function Template for python3

class Solution:
    def trailingZeroes(self, N):
        x=0
        while N//5>0:
            x=x+N//5
            N=N//5
        return x
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)
# } Driver Code Ends