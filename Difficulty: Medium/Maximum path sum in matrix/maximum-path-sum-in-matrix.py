#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        if N == 0:
            return 0
        
        dp = [[0] * N for _ in range(N)]
        
        dp[N-1] = Matrix[N-1]
        for i in range(N-2, -1, -1):
            for j in range(N):
                if j > 0:
                    left_down = dp[i+1][j-1]
                else:
                    left_down = float('-inf')
                
                middle_down = dp[i+1][j]
                
                if j < N-1:
                    right_down = dp[i+1][j+1]
                else:
                    right_down = float('-inf')
                
                dp[i][j] = Matrix[i][j] + max(left_down, middle_down, right_down)
        
        ans = float('-inf')
        for j in range(N):
            ans = max(ans, dp[0][j])
        
        return ans

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends