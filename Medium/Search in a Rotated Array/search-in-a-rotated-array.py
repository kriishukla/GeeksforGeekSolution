#User function Template for python3
class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        while(l<=h):
            mid=l+(h-l)//2
            
            if(A[mid]==key):
                return mid
            
            elif(A[mid]>=A[0]):
                if A[l]<=key and A[mid]>key:
                    h=mid-1
                else:
                    l=mid+1
            
            else:
                if A[mid]<key and A[h]>=key:
                    l=mid+1
                else:
                    h=mid-1
                    
        return -1           
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends