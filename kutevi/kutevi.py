from functools import lru_cache


@lru_cache(maxsize=None)
def dp(sum):
    if sum == 0:
        return True
    if sum < 0 or sum >= 360:
        return False

    is_computing[sum] = True
    for angle in mirko:
        angle_add = sum + angle
        if angle_add >= 360:
            angle_add -= 360
        angle_subtract = abs(sum - angle)

        if (not is_computing[angle_add] and dp(angle_add)) or (not is_computing[angle_subtract] and dp(angle_subtract)):
            is_computing[sum] = False
            return True

    is_computing[sum] = False
    return False

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    mirko = list(map(int, input().split()))
    slavko = list(map(int, input().split()))

    is_computing = [False] * 360

    for s in slavko:
        print('YES' if dp(s) else 'NO')

