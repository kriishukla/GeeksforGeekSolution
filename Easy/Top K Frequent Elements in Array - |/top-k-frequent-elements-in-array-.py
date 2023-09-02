from collections import defaultdict, Counter

class Solution:
    def topK(self, nums, k):
        counter = Counter(nums)
        sorted_nums = sorted(counter.keys(), key=lambda x: (-counter[x], -x))
        return sorted_nums[:k]




#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends