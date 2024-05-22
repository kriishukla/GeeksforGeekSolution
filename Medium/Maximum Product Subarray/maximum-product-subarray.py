#User function Template for python3
class Solution:
    def maxProduct(self, arr, n):
        pre = 1
        suf = 1
        ans = float('-inf') 

        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1

            pre *= arr[i]
            suf *= arr[n - 1 - i]

            ans = max(ans, pre, suf)

        return ans

            
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends