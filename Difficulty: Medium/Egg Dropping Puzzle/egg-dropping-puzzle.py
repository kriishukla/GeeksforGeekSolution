#User function Template for python3


class Solution:
    def eggDrop(self, n, k):
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = 0
            dp[i][1] = 1

        for j in range(1, k + 1):
            dp[0][j] = 0
            dp[1][j] = j
        
        for i in range(2, n + 1):
            for j in range(2, k + 1):
                dp[i][j] = float('inf') 
                for x in range(1, j + 1):
                    attempts = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                    dp[i][j] = min(dp[i][j], attempts)
        return dp[n][k]





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends