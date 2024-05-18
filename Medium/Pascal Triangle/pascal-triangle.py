import math
class Solution:
 
    def nthRowOfPascalTriangle(self,n):
        # code here
        N = [0] * n
        N[0] = 1
        m = pow(10, 9) + 7
        for i in range(1, n):
            for j in range(i, 0, -1): 
                N[j] = (N[j] + N[j - 1]) % m
        return N

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends