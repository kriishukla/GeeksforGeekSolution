class Solution:
    def solve(self, s, t, i, j, memo):

        if i == len(s):
            return len(t) - j
        if j == len(t):
            return len(s) - i
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s[i] == t[j]:
            memo[(i, j)] = self.solve(s, t, i + 1, j + 1, memo)
        else:
            insert = 1 + self.solve(s, t, i, j + 1, memo)
            delete = 1 + self.solve(s, t, i + 1, j, memo)
            replace = 1 + self.solve(s, t, i + 1, j + 1, memo)
            
            memo[(i, j)] = min(insert, delete, replace)
        
        return memo[(i, j)]
    
    def editDistance(self, s, t):
        memo = {}
        return self.solve(s, t, 0, 0, memo)

		# Code here
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends