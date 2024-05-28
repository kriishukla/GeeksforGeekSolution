
class Solution:
    def maxLen(self, n, arr):
        #Code here
        sum = 0
        max_len = 0
    
        sum_index_dict = {}
    
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                max_len = i + 1
            elif sum in sum_index_dict:
                max_len = max(max_len, i - sum_index_dict[sum])
            else:
                sum_index_dict[sum] = i
    
        return max_len
                
            

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends