#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        dp = [0] * (n + 1)  
        for i in range(1, n + 1):
            max_profit = price[i-1]
            for j in range(1, i + 1):
                max_profit = max(max_profit, dp[j] + dp[i - j])
            dp[i] = max_profit
        return dp[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends