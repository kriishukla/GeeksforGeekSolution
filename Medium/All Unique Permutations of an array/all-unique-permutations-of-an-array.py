#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        def perms(arr, path, result):
            if not arr:
                result.add(tuple(path))  
                return
            for i in range(len(arr)):
                perms(arr[:i] + arr[i+1:], path + [arr[i]], result)

        result = set()
        perms(arr, [], result)
        x=[list(t) for t in result]
        x.sort()
        return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends