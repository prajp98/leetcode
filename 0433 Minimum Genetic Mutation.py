def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
    q = deque([(startGene, 0)])
    visit = {startGene}
    while q:
        gene, steps = q.popleft()
        if gene == endGene:
            return steps
        for i in range(8):
            for c in "ACGT":
                new = gene[:i] + c + gene[i + 1:]
                if new in bank and new not in visit:
                    visit.add(new)
                    q.append((new, steps + 1))
    return -1