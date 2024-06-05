'''
    lis[][0]:Petrol 
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,petrolPump, n):
        #Code here
        sum = 0
        for i in range(n):
            sum += petrolPump[i][0] - petrolPump[i][1]
    
        if sum < 0:
            return -1
    
        index = 0
        tank = 0
        for i in range(n):
            tank += petrolPump[i][0] - petrolPump[i][1]
    
            if tank < 0:
                tank = 0
                index = i + 1
    
        return index
#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends