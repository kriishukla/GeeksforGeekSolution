#User function Template for python3


class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if S1[j - 1] == S2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])  
                else:
                    dp[i][j] = 0
        
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends