#User function Template for python3

class Solution:
    def Reduced_String(self, k, s):
        # Your code goes here
        # return the reduced string
        if k==1:
            return ""
        st=[]
        
        for i in range(len(s)):
            if len(st)==0:
                st.append((s[i],1))
  
            
            elif s[i]==st[-1][0]:
                
                f=1+st[-1][1]
                st.append((s[i],f))
                h=st[-1][0]
                if st[-1][1]==k:
                    while len(st)>0 and st[-1][0]==h:

                        st.pop()
                    
            else:
                f=1
                st.append((s[i],f))
        return ''.join([char for char, freq in st])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        k=int(input())
        s=input().strip()
        obj = Solution()
        print(obj.Reduced_String(k,s))

# } Driver Code Ends