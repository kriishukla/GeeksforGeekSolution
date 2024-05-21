
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        n = len(arr)
        
        if n < 1:
            return 0
        ans = 0
        left_max=[0]*n
        right_max=[0]*n
        
        left_max[0] = arr[0]
        
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], arr[i])
            
            
        right_max[-1] = arr[-1]    
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], arr[i])
            
        for i in range(n):
            ans += min(right_max[i], left_max[i])- arr[i]
        
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends