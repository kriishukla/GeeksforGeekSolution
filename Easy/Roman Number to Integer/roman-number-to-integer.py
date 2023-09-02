#User function Template for python3

class Solution:
    def romanToDecimal(self, S):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0

        for i in range(len(S)):
            if i > 0 and roman_numerals[S[i]] > roman_numerals[S[i-1]]:
                number += roman_numerals[S[i]] - 2 * roman_numerals[S[i-1]]
            else:
                number += roman_numerals[S[i]]

        return number




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends