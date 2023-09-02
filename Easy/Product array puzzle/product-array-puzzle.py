#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        product=1
        count=0
        arr=[]
        for i in range (n):
            if nums[i]!=0:
                product*=nums[i]
            else:
                count+=1
        if count==0:
            for i in range(0,n):
                arr.append(product//nums[i])
        if count ==1:
            for i in range(0,n):
                if nums[i]==0:
                    arr.append(product)
                else:
                    arr.append(0)
        if count>=2:
            for i in range (0,n):
                arr.append(0)
        return arr
            
            
                
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends