class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        d=defaultdict(list)

        wordList.append(endWord)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i] + "*" + word[i+1:]
                d[pattern].append(word)
        
        q=deque([beginWord])
        visited=set([beginWord])
        count=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    pattern=word[:j] + "*" + word[j+1:]
                    for nei in d[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            count += 1
        
        return 0