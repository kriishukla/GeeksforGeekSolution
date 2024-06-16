from collections import deque

class Solution:
    def bfs(self, vis, adj, start, color):
        q = deque([start])
        vis[start] = True
        color[start] = 0
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if neighbor not in color: 
                    color[neighbor] = 1 - color[node] 
                    if not vis[neighbor]: 
                        q.append(neighbor)
                        vis[neighbor] = True
                elif color[neighbor] == color[node]:
                    return False  
        
        return True
    
    def isBipartite(self, V, adj):
        vis = [False] * V 
        color = {} 
        
        for i in range(V):
            if not vis[i]: 
                if not self.bfs(vis, adj, i, color):
                    return False 
        
        return True 


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends