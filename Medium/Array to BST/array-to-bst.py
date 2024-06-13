
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def buildtree(temp):
    if len(temp) and len(temp) % 2 == 0:
        n = (len(temp) // 2) - 1
        node = Node(temp[n])
        node.left = buildtree(temp[:n])
        node.right = buildtree(temp[n + 1:])
        return node
    elif len(temp):
        n = len(temp) // 2
        node = Node(temp[n])
        node.left = buildtree(temp[:n])
        node.right = buildtree(temp[n + 1:])
        return node
    return None


class Solution:
	def sortedArrayToBST(self, nums):
	    # code here
	    res = []
	    root = buildtree(nums)
	    
	    def preorder(root):
	        if root == None:
	            return
	        res.append(root.data)
	        preorder(root.left)
	        preorder(root.right)
	        
	    preorder(root)
	   
	    return res

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	nums = list(map(int, input().split()))
	obj = Solution()
	ans = obj.sortedArrayToBST(nums)
	for _ in ans:
		print(_, end = " ")
	print()

# } Driver Code Ends