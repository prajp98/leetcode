class WordDistance:

    def __init__(self, words: List[str]):
        self.mapi = defaultdict(list)
        for i, word in enumerate(words):
            self.mapi[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.mapi[word1], self.mapi[word2]
        i, j = 0, 0
        mini = float("inf")

        while i < len(l1) and j < len(l2):
            mini = min(mini, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return mini