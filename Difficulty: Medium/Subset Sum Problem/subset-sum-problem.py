#User function Template for python3

class Solution:
    def isSubsetSum(self, N, arr, sum):
        dp = [[0] * (sum + 1) for _ in range(N + 1)]
        
        for i in range(N + 1):
            dp[i][0] = 1
        
        for i in range(1, N + 1):
            for j in range(1, sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[N][sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends