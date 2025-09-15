from typing import List  # Не забудьте импортировать List для аннотаций типов


class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #
    #   dp = [0] * (len(cost)+1)
    #   dp[0] = cost[0]
    #   dp[1] = cost[1]
    #
    #   for i in range(2, len(cost) + 1):
    #     dp[i] = (0 if i >= len(cost) else cost[i]) + min(dp[i-1], dp[i-2])
    #
    #   print(dp)
    #
    #   return dp[i]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = 0, 0

        n = len(cost)  # = 3
        dp = [0] * (n + 1)  # dp = [0, 0, 0, 0]

        # Базовые случаи:
        dp[0] = 0  # можем начать с 0-й ступеньки (бесплатно)
        dp[1] = 0  # можем начать с 1-й ступеньки (бесплатно)

        # Заполняем массив:
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        print(dp)

        return dp[n]

    def SolutionDP(self, cost: List) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[0] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]

def main():
    sol = Solution()
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost = [10,15,20]
    print(sol.SolutionDP(cost))

if __name__ == "__main__":
    main()

