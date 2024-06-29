
import heapq

class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        m = len(grid[0])
        cost = [[float('inf')] * m for _ in range(n)]
        cost[0][0] = grid[0][0]

        pq = []
        heapq.heappush(pq, (cost[0][0], (0, 0)))

        row = [0, -1, 0, 1]
        col = [1, 0, -1, 0]

        while pq:
            cst, (i, j) = heapq.heappop(pq)

            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]

                if nr < 0 or nc < 0 or nr >= n or nc >= m:
                    continue

                if cost[nr][nc] > cst + grid[nr][nc]:
                    cost[nr][nc] = cst + grid[nr][nc]
                    heapq.heappush(pq, (cost[nr][nc], (nr, nc)))

        return cost[n - 1][m - 1]



#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends