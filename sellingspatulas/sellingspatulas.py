if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break

        minutes = [-0.08] * 1500
        for _ in range(n):
            m, p = input().split()
            m, p = int(m), float(p)
            minutes[m] += p

        curr_sum, max_sum = 0, 0
        curr_start, curr_length = 0, -1
        start, length = 1500, 1500
        for i in range(m + 1):
            curr_sum += minutes[i]
            curr_length += 1

            if curr_sum > max_sum or \
                    (curr_sum == max_sum and curr_length < length) or \
                    (curr_sum == max_sum and curr_length == length and curr_start < start):
                max_sum, length, start = curr_sum, curr_length, curr_start

            if curr_sum < 10**(-9):
                curr_sum, curr_start, curr_length = 0, i + 1, -1

            # if curr_sum <= 0:
            #     curr_sum, curr_length = 0, 0
            # elif curr_sum > max_sum or (curr_sum == max_sum and curr_length < max_length):
            #     max_sum, max_end, max_length = curr_sum, i, curr_length

        if max_sum <= 0:
            print('no profit')
        else:
            print('{:.2f}'.format(max_sum), start, start + length)

