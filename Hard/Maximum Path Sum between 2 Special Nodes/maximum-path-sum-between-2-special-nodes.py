#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def __init__(self):
        self.res = -1*(2**63 - 1)
    def s(self, root, ischild):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        
        l = self.s(root.left, True)
        r = self.s(root.right, True)
        temp = root.data+l+r
        if root.left is None:
            l = -1*(2**63 - 1)
        if root.right is None:
            r = -1*(2**63 - 1)
        
        
        ans = max(l,r) + root.data
        if root.left is not None and root.right is not None or ischild == False:
            self.res = max(self.res,  temp)
        return ans
        
    def maxPathSum(self, root):
        # code here
        self.s(root, False)
        return self.res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
import sys
sys.setrecursionlimit(10**6)  #Increasing the limit of recursion
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

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.maxPathSum(root))
# } Driver Code Ends