
from collections import deque
import math

class Solution:
    
    def bfs(self, visited, i, j, grid):
        q = deque()
        dirn = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        q.append((i, j))
        visited[i][j] = True
        cnt = 0
        
        while q:
            i, j = q.popleft()
            cnt += 1
            
            for x, y in dirn:
                ni, nj = i + x, j + y
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not visited[ni][nj] and grid[ni][nj] == 1:
                    q.append((ni, nj))
                    visited[ni][nj] = True
                    
        return cnt

    # Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        # Code here
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    max_area = max(self.bfs(visited, i, j, grid), max_area)
                    
        return max_area


#{ 
 # Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends