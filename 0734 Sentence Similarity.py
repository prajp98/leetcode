def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2):
        return False
    pairs = set()
    for pair in similarPairs:
        pairs.add((pair[0], pair[1]))
        pairs.add((pair[1], pair[0]))

    for i in range(len(sentence1)):
        if sentence1[i] != sentence2[i]:
            if (sentence1[i], sentence2[i]) not in pairs:
                return False
    return True