def best_seq(t):
    global N, S, D, T, memo

    if t in memo:
        return memo[t]
    
    memo[t] = 20 ** 9

    for i in range(N+1):
        memo[t] = min(memo[t], D[i] + best_seq(t - S[i]))



if __name__ == '__main__':
    global N, S, D, T, memo
    N, T = list(map(int, input()))
    S, D = [1 for i in range(N+1)] * 2
    memo = {}
    memo[0] = 0
    for i in range(N):
        S[i+1] = int(input())
        D[i+1] = int(input())
        if S[i+1] not in memo or D[i+1] < memo[S[i+1]]:
            memo[S[i+1]] = D[i+1]
