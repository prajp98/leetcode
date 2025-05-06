def alienOrder(self, words: List[str]) -> str:
    graph = defaultdict(set)
    state = {}
    for word in words:
        for c in word:
            state[c] = 0

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
            return ""

        for j in range(minLen):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                break

    res = []

    def dfs(c):
        if state[c] == 1: return False
        if state[c] == 2: return True
        state[c] = 1
        for nei in graph[c]:
            if not dfs(nei):
                return False
        state[c] = 2
        res.append(c)
        return True

    for c in state:
        if state[c] == 0:
            if not dfs(c):
                return ""
    return "".join(reversed(res))