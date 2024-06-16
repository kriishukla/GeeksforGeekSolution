
from collections import OrderedDict
 
class Solution:
    
    def minSwaps(self, nums):
        n=len(nums)
        temp=nums.copy()
        temp.sort()
        track=dict()
        for i in range(n):
            track[nums[i]]=i
        swap=0
        for i in range(n):
            if nums[i]!=temp[i]:
                swap+=1
                a,b=nums[i],temp[i]
                nums[i],nums[track[b]]=nums[track[b]],nums[i]
                track[a],track[b]=track[b],track[a]
        return swap

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends