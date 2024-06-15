#User function Template for python3
    #Function to return a list containing the DFS traversal of the graph.
class Solution:
    def dfsOfGraph(self, V, adj):
        def dfs(visited, adj, s):
            visited[s] = True
            result = [s]
            for i in adj[s]:
                if not visited[i]:
                    result.extend(dfs(visited, adj, i))
            return result
        

        visited = [False] * V
        result = []
        
        for i in range(V):
            if not visited[i]:
                result.extend(dfs(visited, adj, i))
        
        return result


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends