#User function Template for python3
class Solution:
    def rowWithMax1s(self, arr, n, m):
        i = 0
        j = m - 1
        ans = -1
        
        while i < n and j >= 0:
            if arr[i][j] == 0:
                i += 1
            else:
                j -= 1
                ans = i
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends