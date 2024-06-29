#User function Template for python3

class Solution:
    #Function to return the total number of possible unique BST.
    mod=10**9+7
    def numTrees(self,N):
        dp=[None]*(N+1)
        dp[0]=1
        for i in range(1,N+1):
            dp[i]=0
            for j in range(1,i+1):
                dp[i]=(dp[i]+dp[j-1]*dp[i-j])%self.mod
        return dp[N]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n = int(input());
        ob=Solution()
        print(ob.numTrees(n))
# } Driver Code Ends