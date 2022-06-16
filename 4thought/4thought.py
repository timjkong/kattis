import itertools


if __name__ == '__main__':
    m = int(input())

    ans = [0 for _ in range(256+61)]
    perms = [p for p in itertools.product(['*','+','-','//'], repeat=3)]

    for perm in perms:
        s = '4 ' + ' 4 '.join(perm) + ' 4'
        val = int(eval(s))
        s = s.replace('//', '/')
        ans[val + 60] = s + f' = {val}'

    for _ in range(m):
        n = int(input())
        if n < -60 or n > 256 or ans[n+60] == 0:
            print('no solution')
        else:
            print(ans[n+60])
