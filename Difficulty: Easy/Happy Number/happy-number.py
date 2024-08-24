#User function Template for python3

class Solution:

    def isHappy(self, N):

        seen = set()
        
        while N != 1 and N not in seen:
            seen.add(N)
            
            next_number = 0
            while N > 0:
                digit = N % 10
                next_number += digit * digit
                N //= 10

            N = next_number
        
        if N==1:
            return 1
        else:
            return 0

                



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isHappy(N))
# } Driver Code Ends