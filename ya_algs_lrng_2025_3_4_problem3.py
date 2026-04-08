import tracemalloc
from bisect import bisect_right


def bin_search(msv, el):
    left, right = 0, len(msv) - 1

    while left <= right:
        mid = (left + right) // 2

        if msv[mid][0] <= el:
            left = mid + 1  # Ищем первое > el
        else:
            right = mid - 1

    return right  # right — последний <= el


def bin_search2(msv, el):
    # lnght = len(msv)
    # if lnght == 0:
    #     return -1
    # elif lnght == 1:
    #     return 0 if msv[0][0] <= el else -1
    # rng = int(lnght / 2 if lnght % 2 == 0 else (lnght - 1) / 2)
    #
    # if msv[rng][0] > el and msv[rng - 1][0] <= el:
    #         return rng-1
    # elif msv[rng][0] > el:
    #     return bin_search(msv[:rng - 1], el)
    # else:
    #     return rng + bin_search(msv[rng:], el)
    left = 0
    right = len(msv) - 1

    if len(msv) == 1:
        return 0 if msv[0][0] <= el else -1

    while left <= right:
        mid = (left + right)//2

        if mid == 0 and msv[mid][0] > el:
            return -1
        elif mid == 0 and msv[mid][0] <= el:
            left = mid + 1
        elif mid > 0:
            if (msv[mid][0] > el and msv[mid - 1][0] <= el):
                return mid - 1
            elif msv[mid][0] <= el and mid == len(msv) - 1:
                return mid
            elif msv[mid][0] > el:
                right = mid - 1
            elif msv[mid][0] <= el:
                left = mid + 1

    return -1


def main_ya():
    n = int(input())
    intrvls = []
    for i in range(n):
        b, e, w = map(float, input().split())
        intrvls.append((e, b, w))
    intrvls.sort()
    #print(intrvls)
    dp = (n + 1) * [0]
    for i in range(1, n + 1):
        # if i >= 2 and intrvls[i - 1][1] == intrvls[0][1] and intrvls[i - 1][0] == intrvls[0][0]:
        #     prev_i = -1
        # elif i >= 2 and intrvls[i - 1][1] >= intrvls[i-2][0]:
        #     prev_i = i - 2
        # elif i >= 2 and intrvls[i - 1][1] >= intrvls[i-3][0]:
        #     prev_i = i - 3
        # else:
        prev_i = bin_search(intrvls[:(i - 1)], intrvls[i - 1][1])
        # e, b, w = intrvls[i - 1]
        # prev_i = bisect_right(intrvls, (b, e, w))
        dp[i] = max(dp[i - 1], dp[prev_i + 1] + intrvls[i - 1][2])
    #print(dp)

    print(dp[n])


def main_my():
    nmbr = int(input())
    if nmbr == 0:
        print(0)
        return
    tm_intrvl = []
    for i in range(nmbr):
        tm_intrvl.append([float(x) for x in input().split()])
    tm_intrvl.sort(key=lambda x: x[1])

    answrs = []
    answrs.append([tm_intrvl[0][1], tm_intrvl[0][2]])

    for i in range(1, nmbr):
        for j in range(len(answrs)):
            if tm_intrvl[i][1] == answrs[j][0]:
                answrs[j][1] = max(answrs[j][1], tm_intrvl[i][2])
            elif tm_intrvl[i][0] >= answrs[j][0]:
                answrs.append([tm_intrvl[i][1], answrs[j][1] + tm_intrvl[i][2]])
            else:
                answrs.append([tm_intrvl[i][1], tm_intrvl[i][2]])

    print(max(answr[1] for answr in answrs))
    pass


if __name__ == '__main__':
    tracemalloc.start()

    # main_my()
    main_ya()

    # current, peak = tracemalloc.get_traced_memory()
    # tracemalloc.stop()
    #
    # print(f"Текущая память: {current / 1024 ** 2:.2f} MB")
    # print(f"Пик памяти: {peak / 1024 ** 2:.2f} MB")
    # print(f"Потреблено: {(peak - current) / 1024 ** 2:.2f} MB")
