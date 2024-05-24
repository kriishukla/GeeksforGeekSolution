#User function Template for python3

class Solution:

    def spirallyTraverse(self, matrix, r, c):
        arr = []
        first_row = 0
        last_col = c - 1
        last_row = r - 1
        first_col = 0

        while first_row <= last_row and first_col <= last_col:
            # Traverse the top row
            for j in range(first_col, last_col + 1):
                arr.append(matrix[first_row][j])
            first_row += 1

            # Traverse the right column
            for i in range(first_row, last_row + 1):
                arr.append(matrix[i][last_col])
            last_col -= 1

            if first_row <= last_row:
                # Traverse the bottom row
                for j in range(last_col, first_col - 1, -1):
                    arr.append(matrix[last_row][j])
                last_row -= 1

            if first_col <= last_col:
                # Traverse the left column
                for i in range(last_row, first_row - 1, -1):
                    arr.append(matrix[i][first_col])
                first_col += 1

        return arr

        
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends