import sys
from functools import lru_cache



@lru_cache(maxsize=None)
def count_tight_words(s, l):
    global k, n
    if s < 0 or s > k:
        return 0
    if l == n:
        return 1
    return count_tight_words(s + 1, l + 1) + count_tight_words(s, l + 1) + count_tight_words(s - 1, l + 1)


if __name__ == '__main__':
    global k, n
    for line in sys.stdin:
        k, n = list(map(int, line.split()))
        num_tight_words = sum((count_tight_words(s, 1) for s in range(k + 1)))
        print(100 * num_tight_words / ((k + 1) ** n))
        count_tight_words.cache_clear()
