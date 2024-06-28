#User function Template for python3

class Solution:
    # Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        str1 = X
        str2 = Y

        # All we are intrested is in 2 rows (current row and prev row at a time)
        lcs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            char2 = str2[i - 1]
            for j in range(1, m + 1):
                char1 = str1[j - 1]
                if char1 == char2:
                    lcs[1][j] = lcs[0][j - 1] + 1
                else:
                    lcs[1][j] = max(lcs[1][j - 1], lcs[0][j])

            lcs[0], lcs[1] = lcs[1], lcs[0]

        # There was an extra swap at the end of loop so the prev_row, lcs[0] is current row
        return (m + n) - lcs[0][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends