def parse_city_input():
    global n, AL, visited
    n = int(input())
    AL = [[] for _ in range(n)]
    visited = [False] * n
    r = int(input())
    for _ in range(r):
        u, v = list(map(int, input().split()))
        AL[u].append(v)
        AL[v].append(u)

def get_min_roads():
    global n, AL, visited
    ans = 0
    for u in range(n):
        if not visited[u]:
            ans += 1
            dfs(u)
    return ans - 1

def dfs(u):
    visited[u] = True
    for v in AL[u]:
        if not visited[v]:
            dfs(v)


if __name__ == '__main__':
    TC = int(input())
    for _ in range(TC):
        parse_city_input()
        print(get_min_roads())
            
