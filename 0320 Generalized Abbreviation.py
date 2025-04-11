def generateAbbreviations(self, word: str) -> List[str]:
    res = []

    def dfs(i, path, count):
        if i == len(word):
            if count > 0:
                path += str(count)
            res.append(path)
            return
        dfs(i + 1, path, count + 1)
        if count > 0:
            path += str(count)
        dfs(i + 1, path + word[i], 0)

    dfs(0, "", 0)
    return res