#User function Template for python3
class Solution:
    def dfs_topo(self, src, adj, visited, topo):
        visited[src] = 1

        for neighbor in adj[src]:
            if visited[neighbor] == 0:
                self.dfs_topo(neighbor, adj, visited, topo)

        topo.append(src)

    def findOrder(self, alien_dict, n, k):
        adj = [[] for _ in range(k)]

        for i in range(n - 1):
            s1 = alien_dict[i]
            s2 = alien_dict[i + 1]
            sml = min(len(s1), len(s2))
            for j in range(sml):
                if s1[j] != s2[j]:
                    adj[ord(s1[j]) - 97].append(ord(s2[j]) - 97)
                    break

        visited = [0] * k
        topo = []

        for i in range(k):
            if visited[i] == 0:
                self.dfs_topo(i, adj, visited, topo)

        ans = [chr(97 + j) for j in reversed(topo)]
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends