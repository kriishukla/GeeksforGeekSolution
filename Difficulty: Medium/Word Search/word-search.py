class Solution:
    def isWordExist(self, board, word):
        row = len(board)
        col = len(board[0])
        n = len(word)
        def helper(x,y,index,string):
            if index == n:
                return 1
            if x<0 or x>=row or y<0 or y>=col:
                return 0
            if string[index] != board[x][y]:
                return 0
            temp = board[x][y]
            board[x][y] = -1
            top = bottom = left = right = 0
            top = helper(x-1,y,index+1,string)
            bottom = helper(x+1,y,index+1,string)
            left = helper(x,y-1,index+1,string)
            right = helper(x,y+1,index+1,string)
            board[x][y] = temp
            return top or bottom or left or right
        index_array = []
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    index_array.append([i,j])
        for i in index_array:
            if helper(i[0],i[1],0,word):
                return 1
        return 0
#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n, m = map(int, input().split())
		board = []
		for i in range(n):
			a = list(input().strip().split())
			b = []
			for j in range(m):
				b.append(a[j][0])
			board.append(b)
		word = input().strip()
		obj = Solution()
		ans = obj.isWordExist(board, word)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends