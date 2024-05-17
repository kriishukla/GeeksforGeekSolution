#User function Template for python3

class Solution:
    def findNth(self, N):
        if N == 0:
            return "0"
        
        result = []
        while N > 0:
            x = N % 9
            result.append(str(x))
            N = N // 9

        result.reverse()
        return ''.join(result)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
# } Driver Code Ends