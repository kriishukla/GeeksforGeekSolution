#User function Template for python3
from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        low = 0
        high = len(a) - 1
        while high > low:
            mid = (high + low) // 2
            if a[mid] > a[mid + 1] and a[mid] > a[mid - 1]:
                return a[mid]
            elif a[mid] < a[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        return a[high] 
		        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends