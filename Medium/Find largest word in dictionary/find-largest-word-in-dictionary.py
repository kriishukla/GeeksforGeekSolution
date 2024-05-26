#User function Template for python3
class Solution:
    
    def __init__(self):
        self.res = ""

    def check(self, d, s):
        i, j = 0, 0
        while i < len(d) and j < len(s):
            if d[i] == s[j]:
                i += 1
            j += 1
        if i == len(d) and len(self.res) < len(d):
            self.res = d

    def findLongestWord(self, S, d):
        d.sort()
        for word in d:
            self.check(word, S)
        return self.res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n = int(n)
        d = input().split()
        for itr in range(n):
            d[itr] = d[itr]
        S = input()

        ob = Solution()
        print(ob.findLongestWord(S, d))

# } Driver Code Ends