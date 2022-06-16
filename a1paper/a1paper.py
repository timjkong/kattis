def tape():
    ans = 0
    num_required = 2
    for i in range(n-1):
        ans += (num_required / 2) * (2 ** long_sides[i])
        if num_required <= num_sheets[i]:
            break
        if i == n - 2:
            return 'impossible'
        num_required = (num_required - num_sheets[i]) * 2
    return ans



if __name__ == '__main__':
    n = int(input())
    num_sheets = list(map(int, input().split()))
    long_sides = [-3/4 - i/2 for i in range(n)]
    print(tape())