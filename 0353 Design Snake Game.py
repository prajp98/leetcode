class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        self.snake = deque([(0, 0)])
        self.visit = {(0, 0)}
        self.directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

    def move(self, direction: str) -> int:
        head_r, head_c = self.snake[0]
        dr, dc = self.directions[direction]
        r,c = head_r + dr, head_c + dc

        # Check wall collision
        if not (0 <= r < self.height and 0 <= c < self.width):
            return -1

        # Remove tail (may move forward)
        tail = self.snake.pop()
        self.visit.remove(tail)

        # Check self-collision
        if (r,c) in self.visit:
            return -1

        # Add new head
        self.snake.appendleft((r,c))
        self.visit.add((r,c))

        # Check if food is eaten
        if self.score < len(self.food) and (r,c) == tuple(self.food[self.score]):
            self.score += 1
            # Add tail back (grow)
            self.snake.append(tail)
            self.visit.add(tail)

        return self.score