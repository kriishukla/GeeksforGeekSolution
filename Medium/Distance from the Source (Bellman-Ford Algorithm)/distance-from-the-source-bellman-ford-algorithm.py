#User function Template for python3

class Solution:
    def bellman_ford(self, V, edges, S):
        dist=[float('inf')]*V
        dist[S]=0
        for _ in range(V):
            for fm,to,ct in edges:
                if dist[to]>dist[fm]+ct:
                    dist[to]=dist[fm]+ct
        for fm,to,ct in edges:
            if dist[to]>dist[fm]+ct:
                return [-1]
        return [x if x<float('inf') else 10**8 for x in dist]


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
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends