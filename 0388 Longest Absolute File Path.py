def lengthLongestPath(self, input: str) -> int:
    maxi = 0
    pathlen = defaultdict(int)
    for line in input.split('\n'):
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxi = max(maxi, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxi