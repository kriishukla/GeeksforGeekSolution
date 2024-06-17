

class Solution:
    
    def dfs(self, grid, i, j, vis):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or vis[i][j] or grid[i][j] == 0:
            return False
        if grid[i][j] == 2:
            return True
        
        vis[i][j] = True
        
        if (self.dfs(grid, i - 1, j, vis) or
            self.dfs(grid, i + 1, j, vis) or
            self.dfs(grid, i, j - 1, vis) or
            self.dfs(grid, i, j + 1, vis)):
            return True
        
        
        return False
    
    def is_Possible(self, grid):
        if not grid:
            return False
        
        n = len(grid)
        m = len(grid[0])
        
        vis = [[False] * m for _ in range(n)]
        src = None
        des = None

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    src = (i, j)
                elif grid[i][j] == 2:
                    des = (i, j)
        
        if src is None or des is None:
            return False
        
        return self.dfs(grid, src[0], src[1], vis)


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
	ans = obj.is_Possible(grid)
	if(ans):
		print("1")
	else:
		print("0")

# } Driver Code Ends