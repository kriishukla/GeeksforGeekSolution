#User function Template for python3

class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        def wordBoggle(index, word, m, n, row, col, board, vis):
            if index == len(word):
                return True
            
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            
            if vis[row][col] or word[index] != board[row][col]:
                return False
            
            vis[row][col] = True
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                
                if wordBoggle(index + 1, word, m, n, new_row, new_col, board, vis):
                    return True
            
            vis[row][col] = False
            return False
        
        def searchWord(word, board, m, n):
            vis = [[False] * n for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if word[0] == board[i][j]:
                        if wordBoggle(0, word, m, n, i, j, board, vis):
                            return True
            
            return False

        m = len(board)
        n = len(board[0])
        res = []
        
        for word in dictionary:
            if searchWord(word, board, m, n):
                res.append(word)
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()                               # sorting output
        for i in found:
            print(i,end=' ')
        print()
# } Driver Code Ends