dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def floodfill(i, j):
    global m, n, AM, visited
    visited[i][j] = True
    for c in range(8):
        i_next, j_next = i + dr[c], j + dc[c]
        if i_next < 0 or i_next >= m or j_next < 0 or j_next >= n:
            continue
        if AM[i_next][j_next] == '#' and not visited[i_next][j_next]:
            floodfill(i_next, j_next)

def count_closed_loops():
    global m, n, AM, visited
    count = 0
    for i in range(m):
        for j in range(n):
            if AM[i][j] == '#' and not visited[i][j]:
                floodfill(i, j)
                count += 1
    return count

if __name__ == '__main__':
    global m, n, AM, visited
    m, n = list(map(int, input().split()))
    AM = [list(input()) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    print(count_closed_loops())

