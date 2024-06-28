#User function Template for python3
class Solution:
    def check(self, mid, arr, k):
        partition = 1
        curr_sum = 0
        
        for num in arr:
            if curr_sum + num > mid:
                partition += 1
                curr_sum = num
            else:
                curr_sum += num
        
        return partition
    
    def minTime(self, arr, n, k):
        low = max(arr)  # Minimum possible maximum partition sum
        high = sum(arr)  # Maximum possible maximum partition sum
        
        while low < high:
            mid = (low + high) // 2
            parts = self.check(mid, arr, k)
            
            if parts <= k:
                high = mid
            else:
                low = mid + 1
        
        return high


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends