#User function Template for python3
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        dict1={}
        n=len(s)
        i,j=0,0
        maxi=-1
        while j<n:
            if s[j] not in dict1:
                dict1[s[j]]=1
            else:
                dict1[s[j]]+=1
            
            if len(dict1)<k:
                j+=1
            elif len(dict1)==k:
                maxi=max(maxi,j-i+1)
                j+=1
            elif len(dict1)>k:
                dict1[s[i]]-=1
                if dict1[s[i]]==0:
                    del dict1[s[i]]
                i+=1
                j+=1
        return maxi  
            
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends