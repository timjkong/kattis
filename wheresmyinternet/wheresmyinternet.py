from queue import Queue


def bfs(u):
    global AL, visited
    q = Queue()
    q.put(u)
    while not q.empty():
        u = q.get()
        visited[u] = True
        for v in AL[u]:
            if not visited[v]:
                q.put(v)

if __name__ == '__main__':
    global N, AL, visited
    N, M = list(map(int, input().split()))
    AL = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    for _ in range(M):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        AL[a].append(b)
        AL[b].append(a)

    bfs(0)
    is_connected = True
    for i in range(N):
        if not visited[i]:
            print(i + 1)
            is_connected = False

    if is_connected:
        print('Connected')
