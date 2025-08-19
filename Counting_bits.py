class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = (n + 1) * [None]
        # ans[0] = 0
        for i in range(n + 1):
            ans[i] = str(bin(i)[:2]).count('1')

        return ans