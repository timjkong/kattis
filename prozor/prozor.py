def get_row_sums():
    row_sums = [[0 if pixels[i][j] == '.' else 1 for j in range(s)] for i in range(r)]
    for i in range(r):
        row_sums[i][0] = sum(row_sums[i][1 : k - 1])
    for i in range(r):
        for j in range(1, s - k + 1):
            row_sums[i][j] = row_sums[i][j - 1]
            if pixels[i][j] == '*':
                row_sums[i][j] -= 1
            if pixels[i][j + k - 2] == '*':
                row_sums[i][j] += 1
    return row_sums

def find_window(row_sums):
    max_sum, maxi, maxj = (0,) * 3
    for i in range(r - k + 1):
        for j in range(s - k + 1):
            curr_sum = sum((row_sums[i + x][j] for x in range(1, k - 1)))
            if curr_sum > max_sum:
                max_sum, maxi, maxj = curr_sum, i, j
    return max_sum, maxi, maxj

def update_pixels(maxi, maxj):
    for i, j in ((0, 0), (0, k - 1), (k - 1, 0), (k - 1, k - 1)):
        pixels[maxi + i][maxj + j] = '+'

    for i in range(1, k - 1):
        pixels[maxi + i][maxj] = '|'
        pixels[maxi + i][maxj + k - 1] = '|'
        pixels[maxi][maxj + i] = '-'
        pixels[maxi + k - 1][maxj + i] = '-'


if __name__ == '__main__':
    r, s, k = list(map(int, input().split()))
    pixels = [list(input()) for _ in range(r)]
    
    # row_sums[i][j] = sum(row_sums[i][j + 1 :j + k - 1])
    row_sums = get_row_sums()

    # find window area with most flies
    max_sum, maxi, maxj = find_window(row_sums)

    # update pixels
    update_pixels(maxi, maxj)

    print(max_sum)
    for row in pixels:
        print(''.join(row))
