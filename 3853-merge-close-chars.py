import unittest


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        out = ""
        for idx, char in enumerate(s):
            # If char is NOT a copy of an earlier character, include it in the output
            previous_k_chars = set(out[-k:])
            if char not in previous_k_chars:
                out += char

        return out


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
