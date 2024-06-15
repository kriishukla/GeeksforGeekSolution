#User function Template for python3
from typing import List
from collections import deque
class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q = deque()
        q.append(0)
        visited = [False] * V  # Initialize all nodes as not visited
        visited[0] = True
        bfs_traversal = []

        while q:
            current_node = q.popleft()
            bfs_traversal.append(current_node)  # Append current node to traversal path
            
            for neighbour in adj[current_node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)
                    
        return bfs_traversal


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends