#User function Template for python3
class Solution:
    def findSubArraySum(self, arr, n, k):
        current_sum = 0
        sum_count_dict = {0: 1}
        count = 0

        for i in range(n):
            current_sum += arr[i]

            if (current_sum - k) in sum_count_dict:
                count += sum_count_dict[current_sum - k]
            if current_sum in sum_count_dict:
                sum_count_dict[current_sum] += 1
            else:
                sum_count_dict[current_sum] = 1
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends