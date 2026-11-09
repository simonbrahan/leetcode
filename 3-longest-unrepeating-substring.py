import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_start = 0
        current_end = 0
        current_winner = 0
        chars_seen_at = {}

        for idx, char in enumerate(s):
            if char in chars_seen_at and chars_seen_at[char] >= current_start:
                current_start = chars_seen_at[char] + 1

            current_end = idx
            chars_seen_at[char] = idx
            current_winner = max(current_winner, current_end - current_start + 1)

        return current_winner


class SolutionTests(unittest.TestCase):
    def test_samples(self):
        tests = [
            ["", 0],
            ["abcabcbb", 3],
            ["bbbbb", 1],
            ["pwwkew", 3],
        ]

        s = Solution()

        for input, expect in tests:
            self.assertEqual(
                expect,
                s.lengthOfLongestSubstring(input),
                f'failed with string "{input}"',
            )


if __name__ == "__main__":
    unittest.main()
