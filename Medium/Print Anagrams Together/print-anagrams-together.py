#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        arr = []
        dict = {}
        for i in range(len(words)):
            tup = [0]*26
            for j in range(len(words[i])):
                tup[ord(words[i][j])-ord('a')] += 1
            tup = tuple(tup)
            if tup not in dict:
                dict[tup] = [words[i]]
            else:
                dict[tup].append(words[i])
        for key in dict:
            arr.append(list(dict[key]))
        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends