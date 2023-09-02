#User function Template for python3
class Solution:
    def increment(self, arr, N):
        carry = 1
        for i in range(N - 1, -1, -1):
            digit = arr[i] + carry
            arr[i] = digit % 10
            carry = digit // 10
        if carry:
            arr.insert(0, carry)
        return arr







#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends