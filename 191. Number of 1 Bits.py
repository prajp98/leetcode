from collections import Counter


# 1. Brute Force     T:O(logn)     S:O(1)
def bruteForce(n):
    c = 0
    while n:
        c += n & 1
        n >>= 1
    return c


# 2. Recursive     T:O(logn)     S:O(logn)
def recursive(n):
    if n == 0:
        return 0
    else:
        return (n & 1) + recursive(n >> 1)


# 3. Python Count    T:O(1)     S:O(1)
def pyCount(n):
    return bin(n).count('1')


# 4. Brian Kernighan’s Algorithm    T:O(logn)     S:O(1)
def algo(n):
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res


if __name__ == '__main__':
    x = 11
    print(bruteForce(x))
    print(recursive(x))
    print(pyCount(x))
    print(algo(x))
