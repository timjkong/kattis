a, b, c = sorted(list(map(int, input().split())))
order = input()
ans = (str(a) if i == 'A' else (str(b) if i == 'B' else str(c)) for i in order)
print(' '.join(ans))
