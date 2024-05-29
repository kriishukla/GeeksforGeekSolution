#User function Template for python3

class Solution:
	def canPair(self, nums, k):
		# Code here
		for i in range(len(nums)):
		    nums[i]=nums[i]%k
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in range(k):
            if i not in dict:
                dict[i]=0
        if k%2==0:
            if dict[k//2]%2!=0 or dict[0]%2!=0:
                return False
            else:
                for i in range(1,(k-2)//2+1):
                    if dict[i]!=dict[k-i]:
                        return False
        
        else:
            if dict[0]%2!=0:
                return False
            else:
                for i in range(1,(k-1)//2+1):
                    if dict[i]!=dict[k-i]:
                        return False
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends