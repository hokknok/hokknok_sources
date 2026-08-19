import sys
sys.setrecursionlimit(5000)

n, w, h = map(int, input().split())
a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
kn = 0
# k = max(w / min(a), h / min(b)) / 2
k = 10**9
aw, bh, h_prev = 0, b[0] * k, b[0] * k
k_stop = 0
def bin_recurs():
    global aw, bh, kn, k, h_prev, k_stop
    for i in range(n):
        if a[i] * k + aw <= w and bh <= h and b[i] * k == h_prev:
            if i == n - 1:
                if w - a[i] * k - aw < 10 ** (-6) or round(k_stop, 6) == round(k, 6):
                    print(k)
                    break
                else:
                    # print(k, '', k_stop, '', w - a[i] * k - aw)
                    k, kn, k_stop = k + (k - kn) / 2, k, k
                    aw, bh, h_prev = 0, b[0] * k, b[0] * k
                    bin_recurs()
                    return
            aw += a[i] * k
        elif a[i] * k <= w and bh + b[i] * k <= h:
            if i == n - 1:
                if h - b[i] * k - bh < 10 ** (-6) or round(k_stop, 6) == round(k, 6):
                    print(k)
                    break
                else:
                    # print(k, '', k_stop, '', h - b[i] * k - bh)
                    k, kn, k_stop = k + (k - kn) / 2, k, k
                    aw, bh, h_prev = 0, b[0] * k, b[0] * k
                    bin_recurs()
                    return
            aw = a[i] * k
            bh += b[i] * k
            h_prev = b[i] * k
        else:
            k = (k + kn) / 2
            aw, bh, h_prev = 0, b[0] * k, b[0] * k
            bin_recurs()
            return
bin_recurs()
