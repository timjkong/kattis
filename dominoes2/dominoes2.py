def dfs(u):
    global AL, visited, ans
    if visited[u]:
        return
    ans += 1
    visited[u] = True
    for v in AL[u]:
        dfs(v)



if __name__ == '__main__':
    TC = int(input())
    for _ in range(TC):
        global n, l, AL, visited, ans
        n, m, l = list(map(int, input().split()))
        AL = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for _ in range(m):
            x, y = list(map(int, input().split()))
            AL[x - 1].append(y - 1)
        ans = 0
        for _ in range(l):
            u = int(input()) - 1
            dfs(u)
        print(ans)
