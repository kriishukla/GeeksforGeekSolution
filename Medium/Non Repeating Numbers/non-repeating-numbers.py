#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		xor=0
		for i in range(len(nums)):
		    xor=nums[i]^xor
	    
        rightmost_set_bit = xor & -xor
        

        idx = 0
        while rightmost_set_bit > 1:
            rightmost_set_bit >>= 1
            idx += 1
            
        arr1=[]
        arr2=[]
        for i in range(len(nums)):
            if nums[i]&(1<<idx):
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        xori=0
        xorx=0
        final=[]
        for i in range(len(arr1)):
            xori=arr1[i]^xori
        final.append(xori)
        
        for i in range(len(arr2)):
            xorx=arr2[i]^xorx
        
        final.append(xorx)
        
        final.sort()
        
        return final
            
        
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends