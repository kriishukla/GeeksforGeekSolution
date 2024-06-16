import heapq

class Solution:
    
    def dijkstra(self, V, adj, S):
        dis = [float('inf')] * V
        dis[S] = 0

        pq = [(0, S)]
        
        while pq:
  
            d, b = heapq.heappop(pq)

            for node, dist in adj[b]:
                if dis[b] + dist < dis[node]:
                    dis[node] = dis[b] + dist
                    heapq.heappush(pq, (dis[node], node))
        
        return dis



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends