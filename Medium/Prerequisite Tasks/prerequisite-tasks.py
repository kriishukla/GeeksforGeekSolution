#User function Template for python3
class Solution:
    
    def checkcycle(self, adj, visited, stk, strt):
        visited[strt] = True
        stk[strt] = True
        for i in adj[strt]:
            if not visited[i]:
                if self.checkcycle(adj, visited, stk, i):
                    return True
            elif stk[i]:
                return True
        stk[strt] = False
        return False  
    def isPossible(self, N,P, prerequisites):
        adj = [[] for _ in range(N)]
        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            adj[b].append(a) 
        visited = [False] * N
        stk = [False] * N
        for i in range(N): 
            if not visited[i]:
                if self.checkcycle(adj, visited, stk, i):
                    return False
        return True       
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends