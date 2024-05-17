
from typing import List


class Solution:
    def findPair(self, n, x, arr):
        num_set = set()
        for num in arr:
            # Check if the pair (num + x) or (num - x) exists
            if (num + x) in num_set or (num - x) in num_set:
                return 1
            num_set.add(num)
        return -1


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.findPair(n, x, arr)

        print(res)

# } Driver Code Ends