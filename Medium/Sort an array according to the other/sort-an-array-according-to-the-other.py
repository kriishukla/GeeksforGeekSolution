#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
            # Your Code Here
            r_sort=[]
            d1={}
           
            for i in range(N):
                
                d1[A1[i]]=d1.get(A1[i],0)+1
           
            for ele in A2:
                if ele in d1:
                    r_sort.extend([ele]*d1[ele])
                    del d1[ele]
                #r_sort.append()
                
            remain_ele=sorted(num for num in d1.keys())
            for ele in remain_ele:
                r_sort.extend([ele]*d1[ele])
            
                
            return r_sort
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends