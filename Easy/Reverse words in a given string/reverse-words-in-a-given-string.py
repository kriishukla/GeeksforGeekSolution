# User function Template for python3

class Solution:
    def reverseWords(self, S):
        x = []
        word_start = 0
        str_rev = ""

        # Find the indices of dot separators
        for i in range(len(S)):
            if S[i] == ".":
                x.append(i)
        if x==[]:
            return S
        else:
        # Reverse the words and construct the reversed string
            str_rev+=S[x[-1]+1:len(S)]
            str_rev+="."
            for i in range(len(x), 0, -1):
                str_rev += S[x[i-2]+1:x[i-1]]  # Add the word between separators
                if i > 1:
                    str_rev += "."  # Add a dot between words (except for the last word)
    
            # Append the first word
            str_rev += S[:x[0]]
            
            return str_rev








#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends