class Solution:
    def dfs(self, i, j, n, m, result, oldColor, newColor):
        if (i < 0 or i >= n or j < 0 or j >= m or result[i][j] == newColor or result[i][j] != oldColor):
            return
        result[i][j] = newColor
        self.dfs(i - 1, j, n, m, result, oldColor, newColor)
        self.dfs(i + 1, j, n, m, result, oldColor, newColor)
        self.dfs(i, j - 1, n, m, result, oldColor, newColor)
        self.dfs(i, j + 1, n, m, result, oldColor, newColor)

    def floodFill(self, image, sr, sc, newColor):
        if not image:
            return image
        n = len(image)
        m = len(image[0])
        
        result = [row[:] for row in image] 
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return result
        
        self.dfs(sr, sc, n, m, result, oldColor, newColor)
        return result


#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends