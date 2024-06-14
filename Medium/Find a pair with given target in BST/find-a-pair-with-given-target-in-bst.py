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
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    

# } Driver Code Ends
#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    # root : the root Node of the given BST
    # target : the target sum
    def isPairPresent(self,root, target): 
        def push_left(stack, node):
            while node is not None:
                stack.append(node)
                node = node.left
        
        def push_right(stack, node):
            while node is not None:
                stack.append(node)
                node = node.right
        
        st1 = []
        st2 = []
        push_left(st1, root)
        push_right(st2, root)
        
        while st1 and st2 and st1[-1] != st2[-1]:
            sum_val = st1[-1].data + st2[-1].data
            if sum_val == target:
                return 1
            elif sum_val < target:
                node = st1.pop()
                push_left(st1, node.right)
            else:
                node = st2.pop()
                push_right(st2, node.left)
        
        return 0


#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        summ = int(input())
        root=buildTree(s)
        print(Solution().isPairPresent(root,summ))
# } Driver Code Ends