#User function Template for python3

class Solution:
    def get(self, x, parent):
        if parent[x] == x:
            return x
        parent[x] = self.get(parent[x], parent)
        return parent[x]
        
    def union(self, x, y, rank, parent):
        rootX = self.get(x, parent)
        rootY = self.get(y, parent)
        
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    def numProvinces(self, adj, V):
        parent = [i for i in range(V)]
        rank = [0] * V
            
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    self.union(i, j, rank, parent)
        
        provinces = len(set(self.get(i, parent) for i in range(V)))
        
        return provinces

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends