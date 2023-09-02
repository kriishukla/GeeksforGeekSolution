
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n <= 1:
            return n
        current = 1 
        prev = 0 
        for i in range(2,n+1):
            temp = current % 1000000007
            current = (current + prev ) % 1000000007
            prev = temp % 1000000007
        return current % 1000000007

        
#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends