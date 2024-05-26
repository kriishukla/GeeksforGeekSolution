#User function Template for python3
class Solution:
    def printMinNumberForPattern(self,s):
        ans = ''
        st = ''
        n = 1
        for i in s:
            st+=str(n)
            if i=='I':
                ans += st[::-1]
                st = ''
            n+=1
        st += str(n)
        ans += st[::-1]
        return ans
            
            
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends