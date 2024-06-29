#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
class Solution:
    def maxChainLen(self, Parr, n):
        Parr.sort(key=lambda pair: pair.b)
        
        max_length = 0
        current_end = float('-inf')  
        
        for pair in Parr:
            if pair.a > current_end:
                max_length += 1
                current_end = pair.b
        
        return max_length

                    
                    
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))
        obj=Solution()
        print(obj.maxChainLen(Parr, n))
# } Driver Code Ends