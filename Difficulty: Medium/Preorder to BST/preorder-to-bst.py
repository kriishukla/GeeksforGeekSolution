#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def Bst(pre, size):
    if size == 0:
        return None
    
    root = Node(pre[0])
    
    for i in range(1, size):
        insert(root, pre[i])
    
    return root

def insert(node, value):
    if node is None:
        return Node(value)
    
    if value < node.data:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
        
    return node
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    t = int(input())

    for _tcs in range(t):
        size = int(input())
        pre = [int(x) for x in input().split()]

        root = Bst(pre, size)

        postOrd(root)
        print()

# } Driver Code Ends