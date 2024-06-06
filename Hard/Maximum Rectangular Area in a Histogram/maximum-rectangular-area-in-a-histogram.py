#User function Template for python3


class Solution:
    def getMaxArea(self, histogram):
        n = len(histogram)
        
        left = [-1] * n
        right = [n] * n
        
        st = []
        for i in range(n):
            while st and histogram[st[-1]] >= histogram[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        
        st = []
        for i in range(n-1, -1, -1):
            while st and histogram[st[-1]] >= histogram[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, width * histogram[i])
        
        return max_area


        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends