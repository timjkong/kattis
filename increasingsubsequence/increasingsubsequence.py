from bisect import bisect_left

inf = 2*(10**9)

def print_ans(prev, end, length):
    seq = [0 for _ in range(length)]
    seq[length - 1] = nums[end]
    for i in range(2, length + 1):
        seq[length - i] = nums[prev[end]]
        end = prev[end]
    
    print(length, *seq)

# Greedy: O(n log k) where k is length of LIS
def LIS_greedy():
    k, lis_end = 0, 0
    L, L_id = [inf] * n, [inf] * n
    prev = [-1] * n

    for i in range(n):
        pos = bisect_left(L, nums[i])
        L[pos], L_id[pos] = nums[i], i
        prev[i] = -1 if pos == 0 else L_id[pos - 1]
        if pos == k:
            k = pos + 1
            lis_end = i
        if pos == k - 1:
            lis_end = i
    
    print_ans(prev, lis_end, k)
    

# DP: O(n^2)
def LIS_dp():
    LIS = [1] * n
    prev = [-1] * n

    end, length = 0, 1
    curr_max = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                seq_length = 1 + LIS[j]
                if seq_length > LIS[i] or (seq_length == LIS[i] and nums[j] < nums[prev[i]]):
                    LIS[i] = seq_length
                    prev[i] = j
        if LIS[i] > length or (LIS[i] == length and nums[i] < curr_max):
            end, length, curr_max = i, LIS[i], nums[i]
    
    print_ans(length, end)

if __name__ == '__main__':
    while True:
        x = input()
        if x == '0':
            break
        nums = list(map(int, x.split()))
        n = nums[0]
        nums = nums[1:]
        
        # LIS_dp()
        LIS_greedy()
            

