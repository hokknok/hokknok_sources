import sys


def main():
    n = int(input())

    v = [0] * n
    v[:3] = 1, 2, 4

    for i in range(3, n):
        v[i] = v[i - 1] + v[i - 2] + v[i - 3]

    print(v[n-1])

if __name__ == '__main__':
    main()
