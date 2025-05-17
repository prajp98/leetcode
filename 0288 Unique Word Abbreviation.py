class ValidWordAbbr:
    def __init__(self, dictionary: list[str]):
        self.map = {}
        self.words = set(dictionary)
        for word in self.words:
            abbr = self._abbr(word)
            if abbr not in self.map:
                self.map[abbr] = word
            else:
                if self.map[abbr] != word:
                    self.map[abbr] = ""
        print(self.map)

    def isUnique(self, word: str) -> bool:
        abbr = self._abbr(word)
        return abbr not in self.map or self.map[abbr] == word

    def _abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0]+str(len(word) - 2)+word[-1]