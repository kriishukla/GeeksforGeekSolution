#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        if s[0].isdigit() or s[0]=="-":
            for char in s[1:]:
                if not char.isdigit():
                    return -1
            return int(s)
        else:
            return -1
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends