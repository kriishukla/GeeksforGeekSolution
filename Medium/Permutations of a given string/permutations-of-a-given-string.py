#User function Template for python3

class Solution:
    def find_permutation(self, S):
        if len(S) == 0:
            return ['']  
        
        permutations = []
        for i in range(len(S)):
            current_char = S[i]
            remaining = S[:i] + S[i+1:]
            for p in self.find_permutation(remaining):
                permutations.append(current_char + p)
        permutations=list(set(permutations))
        return permutations




#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends