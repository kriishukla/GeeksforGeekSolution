# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self, pattern, string):
        s = 0  # cursor for traversal in string
        p = 0  # cursor for traversal in pattern
        starIdx = -1  # record the position of the last '*' in pattern
        match = 0  # the position in string where we start to match after a '*'

        # Traverse through the string
        while s < len(string):
            # Case 1: characters match or pattern character is '?'
            if p < len(pattern) and (pattern[p] == string[s] or pattern[p] == '?'):
                p += 1
                s += 1
            # Case 2: pattern character is '*'
            elif p < len(pattern) and pattern[p] == '*':
                starIdx = p
                p += 1
                match = s
            # Case 3: there was a previous '*', try to match more characters
            elif starIdx != -1:
                match += 1
                s = match
                p = starIdx + 1
            # Case 4: characters do not match and no '*' to adjust
            else:
                return False
        
        # Check for remaining '*' in pattern
        while p < len(pattern) and pattern[p] == '*':
            p += 1
        
        # If we have traversed the whole pattern, return True
        return p == len(pattern)

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends