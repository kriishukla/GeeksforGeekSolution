#User function Template for python3

def first_occurrence(arr, low, high,n):
    if low > high:
        return -1

    mid = (low + high) // 2

    if n>arr[mid]:
        return first_occurrence(arr, mid+1, high,n)
    elif n<arr[mid]:
        return first_occurrence(arr, low, mid-1,n)
    else:
        if mid == 0 or arr[mid-1]!=arr[mid]:
            return mid
        else:
            return first_occurrence(arr,low,mid-1,n)


def last_occurrence(arr, low, high, n):
    if low > high:
        return -1

    mid = (low + high) // 2

    if n > arr[mid]:
        return last_occurrence(arr, mid + 1, high, n)
    elif n < arr[mid]:
        return last_occurrence(arr, low, mid - 1, n)
    else:
        if mid == high or arr[mid + 1] != arr[mid]:
            return mid
        else:
            return last_occurrence(arr, mid + 1, high, n)
            
            
class Solution:
    def indexes(self, v, x):
        # Your code goes here
        a=first_occurrence(v,0,len(v)-1,x)
        b=last_occurrence(v, 0, len(v)-1, x)
        return  a,b
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends