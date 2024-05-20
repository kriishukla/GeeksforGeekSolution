#User function Template for python3

class Solution:
    def graycode(self,n):
        #code here
        if n==1:
            return ['0','1']
        
        recAns = self.graycode(n - 1)
     
        mainAns = []

        for i in range(len(recAns)):
            s = recAns[i]
            mainAns.append("0" + s)
     
  
        for i in range(len(recAns) - 1, -1, -1):
            s = recAns[i]
            mainAns.append("1" + s)
     
        return mainAns

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        l=ob.graycode(n)
        
        for x in l:
            print(x, end=" ")
            
        print()
     
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends