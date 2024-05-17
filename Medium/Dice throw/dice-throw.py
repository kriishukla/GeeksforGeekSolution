#User function Template for python3

class Solution:

    def noOfWays(self, M, N, X):
        # Initialize a DP table with all zeros
        dp = [[0 for _ in range(X + 1)] for _ in range(N + 1)]
        
        # There is 1 way to achieve sum 0 with 0 dice
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, N + 1):  # Number of dice
            for j in range(1, X + 1):  # Sum
                dp[i][j] = 0
                for k in range(1, M + 1):  # Faces of the dice
                    if j >= k:
                        dp[i][j] += dp[i - 1][j - k]
        
        return dp[N][X]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        M,N,X=map(int,input().split())
        
        ob = Solution()
        print(ob.noOfWays(M,N,X))
# } Driver Code Ends