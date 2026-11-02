import unittest


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        s_len = len(s)
        for i in range(s_len):
            check_range = min(s_len, i + k + 1)
            for j in range(i + 1, check_range):
                if s[j] == s[i]:
                    return self.mergeCharacters(s[:j] + s[j + 1 :], k)

        return s


class SolutionTest(unittest.TestCase):

    def test_no_changes(self):
        solution = Solution()
        self.assertEqual("abc", solution.mergeCharacters("abc", 2))

    def test_short(self):
        solution = Solution()
        self.assertEqual("x", solution.mergeCharacters("xx", 2))

    def test_chop_end(self):
        solution = Solution()
        self.assertEqual("abc", solution.mergeCharacters("abca", 3))

    def test_chop_start(self):
        solution = Solution()
        self.assertEqual("abca", solution.mergeCharacters("aabca", 2))

    def test_chop_middle(self):
        solution = Solution()
        self.assertEqual("ybzybz", solution.mergeCharacters("yybyzybz", 2))


if __name__ == "__main__":
    unittest.main()
