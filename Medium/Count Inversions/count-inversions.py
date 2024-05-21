class Solution:

    def merge(self, arr, l, m, r):
        le = arr[l:m+1]
        ri = arr[m+1:r+1]

        i, j = 0, 0
        k = l
        inversions = 0

        while i < len(le) and j < len(ri):
            if le[i] <= ri[j]:
                arr[k] = le[i]
                i += 1
            else:
                arr[k] = ri[j]
                j += 1
                inversions += (m - l + 1 - i)  # All remaining elements in left array are inversions
            k += 1

        while i < len(le):
            arr[k] = le[i]
            i += 1
            k += 1

        while j < len(ri):
            arr[k] = ri[j]
            j += 1
            k += 1

        return inversions

    def mergeSort(self, arr, l, r):
        inversions = 0
        if l < r:
            mid = (l + r) // 2
            inversions += self.mergeSort(arr, l, mid)
            inversions += self.mergeSort(arr, mid + 1, r)
            inversions += self.merge(arr, l, mid, r)
        return inversions

    def inversionCount(self, arr, n):
        return self.mergeSort(arr, 0, n - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends