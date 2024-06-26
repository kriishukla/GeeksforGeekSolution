#User function Template for python3

class stack:
    def __init__(self):
        self.s = []
        self.minEle = None
        self.mini = []

    def push(self, x):
        self.s.append(x)
        if not self.mini or x < self.mini[-1][0]:
            self.mini.append((x, len(self.s) - 1))

    def pop(self):
        if not self.s:
            return -1
        if len(self.s) - 1 == self.mini[-1][1]:
            self.mini.pop()
        return self.s.pop()

    def getMin(self):
        if not self.mini:
            return -1
        return self.mini[-1][0]
        


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends