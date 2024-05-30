class Solution:
	def overlappedInterval(self, arr):
		#Code here
		arr.sort()
		li=[[arr[0][0],arr[0][1]]]
		for i in range(1,len(arr)):
		    if arr[i][0]<=li[len(li)-1][1]:
		        li[len(li)-1][0]=(min(arr[i][0],li[len(li)-1][0]))
		        li[len(li)-1][1]=(max(arr[i][1],li[len(li)-1][1]))
		    else:
		        li.append([arr[i][0],arr[i][1]])
        return li
#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends