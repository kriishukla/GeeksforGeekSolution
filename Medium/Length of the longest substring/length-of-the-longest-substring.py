#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        last_seen = [-1] * 256
        max_len = 0
        start = 0  

        for end in range(len(S)):
            if last_seen[ord(S[end])] >= start:
                start = last_seen[ord(S[end])] + 1
            last_seen[ord(S[end])] = end
            
            
            max_len = max(max_len, end - start + 1)

        return max_len
                    
                    
                    
                    
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends