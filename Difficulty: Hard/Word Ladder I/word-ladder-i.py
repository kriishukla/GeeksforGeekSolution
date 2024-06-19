from collections import deque

class Solution:
    
    def bfs(self, startWord, targetWord, wordList):
        wordList = set(wordList)
        queue = deque([(startWord, 1)]) 
        
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == targetWord:
                return level
            
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != current_word[i]:
                        new_word = current_word[:i] + c + current_word[i+1:]
                        
                        if new_word in wordList:
                            queue.append((new_word, level + 1))
                            wordList.remove(new_word) 
        
        return 0
    
    def wordLadderLength(self, startWord, targetWord, wordList):    
        return self.bfs(startWord, targetWord, wordList)



#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends