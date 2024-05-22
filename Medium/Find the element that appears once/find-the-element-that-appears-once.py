#User function Template for python3
class Solution:
    def search(self, A, N):
        low = 0
        high = N - 1
        
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or A[mid] != A[mid - 1]) and (mid == N - 1 or A[mid] != A[mid + 1]):
                return A[mid]

            if (mid % 2 == 0 and A[mid] == A[mid + 1]) or (mid % 2 == 1 and A[mid] == A[mid - 1]):
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends