#User function Template for python3
class Solution:
    def upperBound(self, x: int, n: int) -> int:
        low = 0
        high = n
        ans = n
    
        while low <= high:
            mid = (low + high) // 2
            f=mid * (mid + 1) // 2
            if  f> n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
    
        return ans

    def distributeCandies(self, N: int, K: int):
        arr = [0] * K
        a = self.upperBound(K,N)
        a=a-1
        cnt = a // K
        ct = a % K

        # Distribute candies up to the found lower bound
        total_candies = 0
        current_candy_count = 1
        for i in range(cnt):
            for j in range(K):
                arr[j] += current_candy_count
                total_candies += current_candy_count
                current_candy_count += 1

        # Distribute remaining candies
        remaining_candies = N - total_candies
        current_child = 0
        current_candy_count = cnt * K + 1

        while remaining_candies > 0:
            if current_child < K:
                arr[current_child] += min(current_candy_count, remaining_candies)
                remaining_candies -= min(current_candy_count, remaining_candies)
                current_child += 1
                current_candy_count += 1
            else:
                break

        return arr

        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        
        ob = Solution()
        res = ob.distributeCandies(N,K)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends