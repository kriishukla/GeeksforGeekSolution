#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        a=[]
        s=list(s)
        st=[]
        for i in range(len(s)):
            if s[i]==".":
                while st:
                    t=st.pop()
                    a.append(t)
                a.append(".")    
            else:
                st.append(s[i])
        while st:
            t=st.pop()
            a.append(t)
        return "".join(a)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends