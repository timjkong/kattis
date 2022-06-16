# 1 if black, 0 if white
def get_color(i, j):
    if i % 2 == 0:
        return j % 2 == 0
    return j % 2 != 0

def get_moves(start_col, start_row, end_col, end_row):
    if start_col == end_col and start_row == end_row:
        return f'0 {start_col} {start_row}'
    j1, j2 = (ord(x) - ord('A') + 1 for x in (start_col, end_col))
    i1, i2 = int(start_row), int(end_row)
    if get_color(i1, j1) != get_color(i2, j2):
        return 'Impossible'
    ans = f' {start_col} {start_row} '
    if abs(i1 - i2) == abs(j1 - j2):
        return '1' + ans + f'{end_col} {end_row}'

    for i3 in range(1, 9):
        j3 = j1 - (i1 - i3)
        if j3 > 0 and j3 < 9 and abs(i1 - i3) == abs(j1 - j3) and abs(i2 - i3) == abs(j2 - j3):
            next_row = i3
            next_col = chr(j3 + ord('A') - 1)
            break
        j3 = j1 + (i1 - i3)
        if j3 > 0 and j3 < 9 and abs(i1 - i3) == abs(j1 - j3) and abs(i2 - i3) == abs(j2 - j3):
            next_row = i3
            next_col = chr(j3 + ord('A') - 1)
            break
    return '2' + ans + f'{next_col} {next_row} {end_col} {end_row}'

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        start_col, start_row, end_col, end_row = input().split()
        print(get_moves(start_col, start_row, end_col, end_row))

