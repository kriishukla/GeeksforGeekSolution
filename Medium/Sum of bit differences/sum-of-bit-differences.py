#User function Template for python3
class Solution:
    def sumBitDifferences(self, arr, n):
        ans = 0

        for i in range(32):
            count = 0
            for j in range(n):
                if (arr[j] & (1 << i)):
                    count += 1
            ans += count * (n - count)

        return ans * 2
    	            
    	            



#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends