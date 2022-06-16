from bisect import bisect

inf = 2*(10**9)

class WidthHeightPair:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Order by descending width and break ties by ascending height
    def __lt__(self, other):
        if self.width == other.width:
            return self.height < other.height
        return self.width > other.width

# Longest non-decreasing subsequence
def LIS(A, n):
    k = 0
    L, L_id = [inf] * n, [inf] * n
    for i in range(n):
        pos = bisect(L, A[i])
        L[pos], L_id[pos] = A[i], i
        if pos == k:
            k = pos + 1

    return k

'''
Find largest set of dolls that don't fit each other.
This corresponds to largest set of dolls such that for all pairs of dolls i, j in the set,
width[i] >= width[j] and height[i] <= height[j] OR
width[i] <= width[j] and height[i] >= height[j]
Sort widths in descending order then order heights by this order.
For all i < j, widths[i] >= widths[j]
=> if widths[i] == widths[j] or heights[i] <= heights[j], i and j dont fit in one another
=> longest non-decreasing subsequence of heights is equal to largest set of dolls that dont fit in one another
'''
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        wh = list(map(int, input().split()))
        pairs = [WidthHeightPair(wh[i], wh[i + 1]) for i in range(0, n * 2, 2)]
        pairs.sort()
        
        ordered_heights = [p.height for p in pairs]
        print(LIS(ordered_heights, n))


