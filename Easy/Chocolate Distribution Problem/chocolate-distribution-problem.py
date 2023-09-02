#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        min=10**9+1
        for i in range(0,len(A)-M+1):
            if min>A[M-1+i]-A[i]:
                min=A[M-1+i]-A[i]
        return min

        # code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends