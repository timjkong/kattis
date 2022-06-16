MOD = 10 ** 9 + 7
MEM = [2 ** i for i in range(10)]

def mod_pow2(n):
    while n >= len(MEM):
        MEM.append((MEM[-1] * 2) % MOD)
    return MEM[n]


def inversions(seq):
    total, zeros, questions = (0,) * 3
    for x in reversed(seq):
        if x == '1':
            z = zeros * mod_pow2(questions)
            q = questions * mod_pow2(questions - 1)
            total = (total + z + q) % MOD
        elif x == '0':
            zeros += 1
        else:
            total *= 2
            z = zeros * mod_pow2(questions)
            q = questions * mod_pow2(questions - 1)
            total = (total + z + q) % MOD
            questions += 1
    return total

if __name__ == '__main__':
    print(inversions(input()))
