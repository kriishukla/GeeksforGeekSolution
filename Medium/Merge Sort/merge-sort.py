#User function Template for python3

class Solution:
    def merge(self, arr, l, m, r): 
        le = arr[l:m+1]
        ri = arr[m+1:r+1]
        
        i, j = 0, 0
        k = l

        while i < len(le) and j < len(ri):
            if le[i] <= ri[j]:
                arr[k] = le[i]
                i += 1
            else:
                arr[k] = ri[j]
                j += 1
            k += 1

        while i < len(le):
            arr[k] = le[i]
            i += 1
            k += 1
        
        while j < len(ri):
            arr[k] = ri[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends