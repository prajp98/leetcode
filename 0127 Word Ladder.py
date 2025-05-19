def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    if endWord not in wordList:
        return 0
    q = deque([beginWord])
    visit = {beginWord}
    level = 1
    while q:
        for _ in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # extra O(m)
                    new = word[:i] + c + word[i + 1:]
                    if new in wordList and new not in visit:
                        visit.add(new)
                        q.append(new)
        level += 1
    return 0