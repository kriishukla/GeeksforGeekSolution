
from typing import List

class Solution:
    
    def dfs(self, node, adj, parent, visited):
        visited[node] = parent
        for i in adj[node]:
            if not visited[i]:
                if self.dfs(i, adj, node, visited):
                    return True
            elif visited[i] and i != parent:
                return True
        return False
                
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V
        
        for node in range(V):
            if not visited[node]:
                if self.dfs(node, adj, -1, visited):
                    return True
                    
        return False

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends