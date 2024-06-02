#User function Template for python3

# design the class in the most optimal way

class DDL:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
      
     
    def __init__(self,cap):
        self.cap = cap
        self.mapp = {}
        self.head = DDL(0,0)
        self.tail = DDL(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.sz = 0
        
    def delete_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
       
        
        
        
    def add_to_head (self,node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
    
    def get(self, key):
        if key in self.mapp:
            node = self.mapp[key]
            result = node.val
            self.delete_node(node)
            self.add_to_head(node)
            return result
        else:
            return -1
            
    def set(self, key, value):
        if  key in self.mapp:
            node = self.mapp[key]
            node.val = value
            self.delete_node(node)
            self.add_to_head(node)
        else:
            node = DDL(key,value)
            self.mapp[key] = node
            if self.sz < self.cap:
                self.sz+=1
                self.add_to_head(node)
            else:
                del self.mapp[self.tail.prev.key]
                self.delete_node(self.tail.prev)
                self.add_to_head(node)
        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends