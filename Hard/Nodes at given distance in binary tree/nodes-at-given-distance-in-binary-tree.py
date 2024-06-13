#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# Solution Class Definition
class Solution:
    def __init__(self):
        pass
    
    # Utility function to create a new Tree Node
    def newNode(self, val):
        return Node(val)
    
    # Function to Build Tree
    def buildTree(self, s):
        if len(s) == 0 or s[0] == 'N':
            return None
        
        ip = s.split()
        root = self.newNode(int(ip[0]))
        queue = []
        queue.append(root)
        i = 1
        while len(queue) > 0 and i < len(ip):
            currNode = queue.pop(0)
            currVal = ip[i]
            if currVal != 'N':
                currNode.left = self.newNode(int(currVal))
                queue.append(currNode.left)
            i += 1
            if i >= len(ip):
                break
            currVal = ip[i]
            if currVal != 'N':
                currNode.right = self.newNode(int(currVal))
                queue.append(currNode.right)
            i += 1
        return root
    
    def createmapping(self, root, cm, target):
        q = []
        q.append(root)
        cm[root] = None
        ans = None
        
        while len(q) > 0:
            temp = q.pop(0)
            if temp.data == target:
                ans = temp
            if temp.left:
                cm[temp.left] = temp
                q.append(temp.left)
            if temp.right:
                cm[temp.right] = temp
                q.append(temp.right)
        return ans
    
    def check(self, startNode, visited, ans, k, cm):
        if k == 0 or startNode is None:
            if startNode:
                ans.append(startNode.data)
            return
        
        visited[startNode] = True
        
        if not visited.get(startNode.left, False) and startNode.left:
            self.check(startNode.left, visited, ans, k - 1, cm)
        
        if not visited.get(startNode.right, False) and startNode.right:
            self.check(startNode.right, visited, ans, k - 1, cm)
        
        if not visited.get(cm[startNode], False) and cm[startNode]:
            self.check(cm[startNode], visited, ans, k - 1, cm)
    
    def KDistanceNodes(self, root, target, k):
        ans = []
        cm = {}
        st = self.createmapping(root, cm, target)
        visited = {}
        self.check(st, visited, ans, k, cm)
        ans.sort()
        return ans


        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends