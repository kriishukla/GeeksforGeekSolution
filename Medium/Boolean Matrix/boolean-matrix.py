#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here 
    lny = len(matrix)
    
    lnx = len(matrix[0])
    
    cols = set()
    
    rows = set()
    
    for y in range(lny):
        
        for x in range(lnx):
            
            if matrix[y][x] ==1:
                
                cols.add(x)
                
                rows.add(y)
                
                
    for y in range(lny):
        
        for x in range(lnx):
            
            if x in cols or y in rows:
                
                matrix[y][x] =1
    return matrix
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends