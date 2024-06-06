class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
            def helper(s, temp):
                if len(s) == 0:
                    return
            
                char = s.pop()
                helper(s,temp)
              
                while s and s[-1] > char:
                    temp.append(s.pop())
            
                s.append(char)
            
                while temp:
                    s.append(temp.pop())
        
    
            temp = []
            helper(s, temp)



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends