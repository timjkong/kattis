import sys


# def can_sim():
#     # bound p0
#     p0_max = 10000
#     for i in range(3):
#         if dice[0][i] > 0:
#             p0_max = min(p0_max, probs[i] // dice[0][i])

#     for p0 in range(p0_max + 1):
#         rem_amt = [probs[i] - p0 * dice[0][i] for i in range(3)]

#         # bound p1
#         p1_max = 10000 - p0
#         for i in range(3):
#             if dice[1][i] > 0:
#                 p1_max = min(p1_max, rem_amt[i] // dice[1][i])

#         for p1 in range(p1_max + 1):
#             p2 = 10000 - p0 - p1
#             curr_probs = [p0 * dice[0][i] + p1 * dice[1][i] + p2 * dice[2][i] for i in range(3)]
#             if curr_probs == probs:
#                 return 'YES'
#     return 'NO'

def can_sim():
    # bound p0
    p0_max = 9998
    for i in range(3):
        if dice[0][i] > 0:
            p0_max = min(p0_max, probs[i] // dice[0][i])

    for p0 in range(p0_max + 1):
        curr_probs = [p0 * dice[0][i] for i in range(3)]
        rem_amt = [probs[i] - curr_probs[i] for i in range(3)]

        # bound p1
        # p1_max = 10000 - p0
        # for i in range(3):
        #     if dice[1][i] > 0:
        #         p1_max = min(p1_max, rem_amt[i] // dice[1][i])

        l, r = 1, 10000 - p0 - 1

        b=False
        for i in range(3):
            hi = max(dice[1][i], dice[2][i])
            lo = min(dice[1][i], dice[2][i])
            if r * hi + lo < rem_amt[i] or r * lo + hi > rem_amt[i]:
                b = True
                break
        if b:
            continue


        while l <= r:
            p1 = l + (r - l) // 2
            p2 = 10000 - p0 - p1

            rem_probs = [p1 * dice[1][i] + p2 * dice[2][i] for i in range(3)]
            if rem_probs == rem_amt:
                return 'YES'

            if rem_probs[0] < rem_amt[0]:
                if dice[1][0] < dice[2][0]:
                    r = p1 - 1
                elif dice[1][0] > dice[2][0]:
                    l = p1 + 1
                else:
                    break
            elif rem_probs[0] > rem_amt[0]:
                if dice[1][0] < dice[2][0]:
                    l = p1 + 1
                elif dice[1][0] > dice[2][0]:
                    r = p1 - 1
                else:
                    break
            elif rem_probs[1] < rem_amt[1]:
                if dice[1][1] < dice[2][1]:
                    r = p1 - 1
                elif dice[1][1] > dice[2][1]:
                    l = p1 + 1
                else:
                    break
            else:
                if dice[1][1] < dice[2][1]:
                    l = p1 + 1
                elif dice[1][1] > dice[2][1]:
                    r = p1 - 1
                else:
                    break

    return 'NO'



if __name__ == '__main__':
    inputs = iter(sys.stdin.readlines())
    dice = [[] for _ in range(3)]
    b = False

    while True:
        for i in range(3):
            dice[i] = list(map(int, next(inputs).split()))
            if dice[i] == [0,0,0]:
                b=True
                break
        if b:
            break
        probs = list(map(lambda x: int(x) * 10000, next(inputs).split()))
        print(can_sim())
        next(inputs)
    
