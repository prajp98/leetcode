class MagicDictionary:

    def __init__(self):
        self.dict=defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            n=len(word)
            self.dict[n].add(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        for word in self.dict[n]:
            diff = 0
            for i in range(n):
                if word[i] != searchWord[i]:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False

class MagicDictionary:

    def __init__(self):
        self.neighbors = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                self.neighbors[pattern].append(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            pattern = searchWord[:i] + '*' + searchWord[i+1:]
            for word in self.neighbors.get(pattern, []):
                if word != searchWord:
                    return True
        return False