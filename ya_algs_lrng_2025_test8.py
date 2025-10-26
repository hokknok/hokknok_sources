import sys


def main():
    n, m = map(int, input().split())
    strng = input()
    size_slice = int(n/m)
    strng_lst = [strng[i:i+size_slice] for i in range(0, len(strng), size_slice)]

    pcs = []
    for i in range(m):
        pcs.append(input())

    tpl_strng = []
    for i in range(m):
        tpl_strng.append((strng_lst[i], i))
    tpl_strng = sorted(tpl_strng)

    tpl_pcs = []
    for i in range(m):
        tpl_pcs.append((pcs[i],i))
    tpl_pcs = sorted(tpl_pcs)

    ans = [0] * m
    for i in range(m):
        ans[tpl_strng[i][1]] = tpl_pcs[i][1] + 1

    print(*ans)
    return

if __name__ == '__main__':
    main()
