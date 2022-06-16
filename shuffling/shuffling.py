def shuffle(n, type):
    original = [i for i in range(n)]
    curr = original.copy()
    num_shuffles = 0
    while True:
        midpoint = n // 2 if n % 2 == 0 or type == 'in' else n // 2 + 1
        top = curr[:midpoint] if type  == 'out' else curr[midpoint:]
        bottom = curr[:midpoint] if type  == 'in' else curr[midpoint:]
        smaller_len = min(len(top), len(bottom))
        curr = [x for pair in zip(top[:smaller_len], bottom[:smaller_len]) for x in pair]
        if len(top) > smaller_len:
            curr.append(top[-1])
        if len(bottom) > smaller_len:
            curr.append(bottom[-1])
        num_shuffles += 1
        if curr == original:
            break
    return num_shuffles


if __name__ == '__main__':
    n, type = input().split()
    n = int(n)
    print(shuffle(n, type))
