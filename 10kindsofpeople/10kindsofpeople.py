import sys
from collections import deque
from tokenize import group

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
group_id = 1

# def floodfill(r1, c1):
#     global r, c, mp, groups
#     groups[r1][c1] = group_id
#     for i in range(4):
#         r2, c2 = r1 + dr[i], c1 + dc[i]
#         if r2 < 0 or r2 >= r or c2 < 0 or c2 >= c:
#             continue
#         if mp[r2][c2] == mp[r1][c1] and groups[r2][c2] == 0:
#             floodfill(r2, c2)

def floodfill(r1, c1):
    global r, c, mp, groups
    s = deque()
    groups[r1][c1] = group_id
    s.append((r1, c1))
    while s:
        r_curr, c_curr = s.pop()
        groups[r_curr][c_curr] = group_id
        for i in range(4):
            r_next, c_next = r_curr + dr[i], c_curr + dc[i]
            if r_next < 0 or r_next >= r or c_next < 0 or c_next >= c:
                continue
            if mp[r_next][c_next] == mp[r1][c1] and groups[r_next][c_next] == 0:
                groups[r_next][c_next] = group_id
                s.append((r_next, c_next))

if __name__ == '__main__':
    global r, c, mp, groups
    r, c = map(int, input().split())
    mp = [list(input()) for _ in range(r)]

    groups = [[0] * c for _ in range(r)]

    n = int(input())
    for i in range(n):
        r1, c1, r2, c2 = map(lambda x: x - 1, map(int, input().split()))
        for i, j in [(r1, c1), (r2, c2)]:
            if groups[i][j] == 0:
                floodfill(i, j)
                group_id += 1

        if groups[r1][c1] == groups[r2][c2]:
            print('binary' if mp[r1][c1] == '0' else 'decimal')
        else:
            print('neither')
