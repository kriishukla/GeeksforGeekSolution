#User function Template for python3

class Solution:
    def wordBreak(self,n, s, dictionary):
        memo = {}

        def wordBreakHelper(s):
            if s in memo:
                return memo[s]
            if s in dictionary:
                memo[s] = True
                return True

            for i in range(1, len(s)):
                prefix = s[:i]
                suffix = s[i:]

                if prefix in dictionary and wordBreakHelper(suffix):
                    memo[s] = True
                    return True

            memo[s] = False
            return False

        return wordBreakHelper(s)

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends