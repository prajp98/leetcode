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