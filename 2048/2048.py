dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def shift(grid, move):
    merged = [[False] * 4 for _ in range(4)]
    r = range(4) if move <= 1 else range(3, -1, -1)
    for _ in range(4):
        for i in r:
            for j in r:
                if grid[i][j] == 0:
                    continue
                i2, j2 = i + dr[move], j + dc[move]
                if i2 not in range(4) or j2 not in range(4):
                    continue
                if grid[i2][j2] == 0 or (grid[i2][j2] == grid[i][j] and not merged[i][j]):
                    if grid[i2][j2] > 0 or merged[i][j]:
                        merged[i][j] = True
                        merged[i2][j2] = True
                    grid[i2][j2] += grid[i][j]
                    grid[i][j] = 0



if __name__ == '__main__':
    grid = [list(map(int, input().split())) for _ in range(4)]
    move = int(input())
    shift(grid, move)
    for i in range(4):
        print(*grid[i])
    
