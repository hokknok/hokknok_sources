import sys


def main():
    a, b, c, v0, v1, v2 = map(int,(input().split()))

    xa = a / v0
    xa += min(c / v1 + b / v2, a / v1 + b / v0 + b / v1, c / v1 + c / v2 + a / v2, c / v0 + c / v1 + a /v2, a / v1 + a / v0 + c / v0 + c / v1 + a / v1)

    xb = b / v0
    xb += min(c / v1 + a / v2, b / v1 + a / v0 + a / v1, c / v1 + c / v2 + b / v2, c / v0 + c / v1 + b /v2, b / v1 + b / v0 + c / v0 + c / v1 + b / v1)

    print(f"{min(xa, xb):.5f}")

if __name__ == '__main__':
    main()