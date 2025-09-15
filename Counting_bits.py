from typing import List  # Не забудьте импортировать List для аннотаций типов


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            print('i >> 1 = ', i >> 1, 'ans[i >> 1] = ', ans[i >> 1], 'i = ', i)
            ans[i] = ans[i >> 1] + (i & 1)
            print('ans[i] = ', ans[i])
        return ans

def main():
    sol = Solution()

    print(sol.countBits(7))

if __name__ == "__main__":
    main()

