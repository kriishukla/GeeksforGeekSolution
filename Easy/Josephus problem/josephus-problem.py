#{ 
 # Driver Code Starts
import math



# } Driver Code Ends
#Complete this function

class Solution:
    def josephus(self,n,k):
        #Your code here
        if n==1:
            return 1
        return (self.josephus(n - 1, k) + k-1) % n+1
        

#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(Solution().josephus(n,k))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends