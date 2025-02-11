
def numJewelsInStones(jewels: str, stones: str) -> int:
    total=0
    for s in stones:
        for j in jewels:
            if s==j:
                total+=1
    return total

if __name__ == '__main__':
    print(numJewelsInStones("123","123"))