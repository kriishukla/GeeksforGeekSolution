#User function Template for python3

class Solution:
    def longestPalindrome(self, S):
        for i in range(len(S),-1,-1):
            for j in range(len(S)-i+1):
                rev = S[j:j+i]
                if rev == rev[::-1]:
                    return rev


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends