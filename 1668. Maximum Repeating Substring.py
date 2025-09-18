class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = [0] * len(sequence)
        recword = word * (len(sequence) // len(word)) + word[:len(sequence) % len(word)]

        print(recword)

        for i in range(len(recword)):
            for j in range(i, len(sequence)):
                print("i =", i, "j =", j, "recword[i] =", recword[i], "sequence[j]", sequence[j])
                if recword[i] == sequence[j] and count[j - i] == i:
                    count[j - i] += 1
                elif count[j - i] < len(word):
                    count[j - i] = 0

            print(count)

        return max(count) // len(word)


def main():
    repeating = Solution()
    # sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    # word = "aaaba"
    sequence = "ababc"
    word = "ab"

    print(repeating.maxRepeating(sequence, word))


if __name__ == "__main__":
    main()
