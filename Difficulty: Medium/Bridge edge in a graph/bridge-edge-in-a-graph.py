#User function Template for python3

class Solution:
   
    def dfs(self, adj, u, visited):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                self.dfs(adj, v, visited)
    
    def isBridge(self, V, adj, c, d):
        new_adj = [[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                if (u == c and v == d) or (u == d and v == c):
                    continue
                new_adj[u].append(v)
        
        visited = [False] * V
        original_components = 0
        for u in range(V):
            if not visited[u]:
                original_components += 1
                self.dfs(adj, u, visited)
        
        new_visited = [False] * V
        new_components = 0
        for u in range(V):
            if not new_visited[u]:
                new_components += 1
                self.dfs(new_adj, u, new_visited)
        
        if new_components != original_components:
            return 1
        else:
            return 0

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
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends