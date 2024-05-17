#User function Template for python3
class Solution:
    mod=10**9+7
    def numberOfPaths (self, M, N):
        n=M+N-2
        r=min(M-1,N-1)
        num,deno=1,1
        for i in range(1,r+1):
            num*=(n+1-i)
            deno*=i
        return (num//deno)%self.mod
#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends