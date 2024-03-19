#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        
        def dfs(n):
            vis1.add(n)
            for i in adj[n]:
                if i not in vis1:
                    dfs(i)
            q.append(n)

        q=[]            
        vis1=set()
        for i in range(V):
            if i not in vis1:
                dfs(i)

  
        revadj=[[] for i in range(V)]
        for n in range(V):
            for a in adj[n]:
                revadj[a].append(n)
        
        def revdfs(n):
            vis2.add(n)
            for i in revadj[n]:
                if i not in vis2:
                    revdfs(i)


        vis2=set()
        cnt=0
        while q:
            i=q.pop()
            if i not in vis2:
                revdfs(i)
                cnt+=1


        return cnt



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends