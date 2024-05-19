#User function Template for python3

class Solution:
    def subsets(self, A):
        #code here
        
        def subs(inp,out,res):
            if len(inp)==0:
                res.append(out)
                return 
            out1 = out[:]
            out2 = out[:]
            out2.append(inp[0])
            subs(inp[1:],out1,res)
            subs(inp[1:],out2,res)
            return


        res = []
        out = []
        subs(A,out,res)
        return sorted(res)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int, input().strip().split()))

        ob = Solution()
        result = ob.subsets(A)

        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j], end=" ")

            print()

# } Driver Code Ends