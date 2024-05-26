#User function Template for python3

class Solution:
    def findAndReplace(self, S: str, Q: int, index: list, sources: list, targets: list) -> str:
        S_list = list(S)
        
        replacements = sorted(zip(index, sources, targets), reverse=True)
        
        for idx, src, tgt in replacements:

            actual_index = S.find(src, idx, idx + len(src))
            if actual_index == idx:
                S_list[idx:idx + len(src)] = list(tgt)
        
        return ''.join(S_list)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        Q=int(input())
        index=list(map(int,input().split()))
        sources=list(map(str,input().split()))
        targets=list(map(str,input().split()))
        
        ob = Solution()
        print(ob.findAndReplace(S,Q,index,sources,targets))
# } Driver Code Ends