def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
    dist = abs(target[0]) + abs(target[1])
    for ghost in ghosts:
        gdist = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
        if gdist <= dist:
            return False
    return True