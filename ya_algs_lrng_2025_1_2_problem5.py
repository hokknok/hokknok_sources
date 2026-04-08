import sys


def main():
    n, k = map(int, (input().split()))
    # for i in range(k):
    #    if n % 10 == 0:
    #        break
    #    n += n % 10
    if n % 10 != 0:
        if n % 10 == 5:
            n += 5
        else:
            while (n % 10 not in [2, 4, 8, 6]) and k != 0:
                n += n % 10
                k -= 1

            ccl = k // 4
            ost = k % 4
            print("ccl", ccl)
            print("ost", ost)
            for i in range(ost):
                n += n % 10
            n += ccl * 20

    print(n)

if __name__ == '__main__':
    main()
