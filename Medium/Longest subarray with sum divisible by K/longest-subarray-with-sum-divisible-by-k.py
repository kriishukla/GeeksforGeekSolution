#User function Template for python3
class Solution:
    def longSubarrWthSumDivByK(self, arr, n, K):
        cum_sum_dict = {}
        cum_sum = 0
        max_len = 0
    
        for i in range(n):
            cum_sum += arr[i]
            remainder = cum_sum % K
            if remainder < 0:
                remainder += K
            if remainder == 0:
                max_len = i + 1
            elif remainder in cum_sum_dict:
                max_len = max(max_len, i - cum_sum_dict[remainder])
            else:
                cum_sum_dict[remainder] = i
        
        return max_len
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends