#User function Template for python3

class Solution:
    
    #Function to find maximum of minimums of every window size.

     def maxOfMin(self,arr,n):
        left = [-1] * n  # list to store the previous smaller elements
        right = [n] * n  # list to store the next smaller elements
        stack = []
        # Calculating the previous smaller element for each element in the array.
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        # left result -> [-1,0,1,2,-1,4,4]
        # Clearing the stack
        stack = []
        # Calculating the next smaller element for each element in the array.
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        # right result -> [7,4,4,4,7,6,7]
        result = [0] * (n + 1)
        # Calculate the maximum of the minimums for each window size.
        for i in range(n):
            # max window_size of an element between its previous and next smaller elements
            window_size = right[i] - left[i] - 1
            result[window_size] = max(result[window_size], arr[i])
        # result -> [0,70,30,20,0,0,0,10]
        # Fill gaps in the result with closest smaller element
        for i in range(n-1, 0, -1):
            result[i] = max(result[i], result[i+1])
        # result -> [70,70,30,20,10,10,10,10]
        return result[1:]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.maxOfMin(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()

# } Driver Code Ends