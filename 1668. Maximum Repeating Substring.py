class Solution:
    # def maxRepeating(self, sequence: str, word: str) -> int:
    #     count = [0] * len(sequence)
    #     recword = word * (len(sequence) // len(word)) + word[:len(sequence) % len(word)]
    #
    #     for i in range(len(recword)):
    #         for j in range(i, len(sequence)):
    #             if recword[i] == sequence[j] and count[j - i] == i:
    #                 count[j - i] += 1
    #             elif count[j - i] < len(word):
    #                 count[j - i] = 0
    #
    #     return max(count) // len(word)

    def maxRepeating(self, sequence: str, word: str) -> int:
        dp = [0] * len(word)
        mxrptng = 0
        j = 0

        while j < len(sequence):
            for i in range(j, min(j + len(word), len(sequence))):
                # if j == 0:
                #     dp_indx = 0
                # else:
                #     dp_indx = index - 1

                print("j = ", j)
                print("i = ", i)
                index = j%len(word)
                print("index = ", index)
                #dp_indx = i%len(word)
                dp_indx = i - j
                print("dp_indx = ", dp_indx)
                print("word[index] = ", word[index], "sequence[i] = ", sequence[i])
                if word[index] == sequence[i]:
                    print("1 dp[dp_indx] = ", dp[dp_indx])
                    dp[dp_indx] += 1
                    print("2 dp[dp_indx] = ", dp[dp_indx])
                else:
                    print("11 dp[dp_indx] = ", dp[dp_indx])
                    if dp[dp_indx]//len(word) > mxrptng:
                        mxrptng = dp[dp_indx]//len(word)
                    dp[dp_indx] = 0
                    print("22 dp[dp_indx] = ", dp[dp_indx])
            j += 1

        return mxrptng


def main():
    repeating = Solution()
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    #sequence = "ababc"
    #word = "ab"

    print(repeating.maxRepeating(sequence, word))


if __name__ == "__main__":
    main()
