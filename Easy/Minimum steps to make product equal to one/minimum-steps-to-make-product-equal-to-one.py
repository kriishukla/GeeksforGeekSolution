#User function Template for python3

class Solution:
    def makeProductOne(self, arr, N):
        # code here 
        count =0
        trial=0
        x=0
        for i in range(0,N,1):
            if arr[i]<0:
                trial+=(-1)-arr[i]
                count+=1
            elif arr[i]>0:
                trial+=arr[i]-1
            else:
                x+=1
        if count%2!=0 and x==0:
            trial+=2
        else:
            trial=trial+x
        return trial
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.makeProductOne(arr,N))
# } Driver Code Ends