#User function Template for python3

def isValid(s):
    #code here
    s1=s.split(".")
    if len(s1) != 4:  
        return 0
    for i in range(len(s1)):

        if (not (s1[i].isdigit())):
            return 0
        if len(s1[i])>1 and s1[i][0]=="0":

            return 0
        if 0<=int(s1[i])<=255:
            continue
        else:
            return 0
    return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends