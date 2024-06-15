#User function Template for python3

class Solution:
    # Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        
        def merge2sortedarray(arr1, arr2):
            merged_arr = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    merged_arr.append(arr1[i])
                    i += 1
                else:
                    merged_arr.append(arr2[j])
                    j += 1
            merged_arr.extend(arr1[i:])
            merged_arr.extend(arr2[j:])
            return merged_arr
        
        if K == 0 or not arr:
            return []
        
        while K > 1:
            i = 0
            j = K - 1
            while i < j:
                arr[i] = merge2sortedarray(arr[i], arr[j])
                i += 1
                j -= 1
                K -= 1
        return arr[0] if K == 1 else []


    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends