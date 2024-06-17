#User function Template for python3
class Solution:
    
    def findparent(self, x, parent):
        if parent[x] == x:
            return x
        else:
            parent[x] = self.findparent(parent[x], parent)
            return parent[x]
            
    def union(self, x, y, parent, rank):
        rootX = self.findparent(x, parent)
        rootY = self.findparent(y, parent)
        
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
        
    def spanningTree(self, V, adj):
        parent = [i for i in range(V)]
        rank = [0] * V
        edges = []
        
        for u in range(V):
            for v, weight in adj[u]:
                edges.append((u, v, weight))
        
        edges.sort(key=lambda x: x[2])
        
        mst_weight = 0
        
        for u, v, weight in edges:
            if self.findparent(u, parent) != self.findparent(v, parent):
                self.union(u, v, parent, rank)
                mst_weight += weight
        
        return mst_weight


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends