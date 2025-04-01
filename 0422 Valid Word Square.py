def validWordSquare(self, words: List[str]) -> bool:
    for r in range(len(words)):
        for c in range(len(words[r])):
            if c >= len(words) or r >= len(words[c]) or words[r][c] != words[c][r]:
                return False
    return True