import unittest
from collections import Counter, deque


class StackSet:
    def __init__(self, stack_length: int):
        self.stack_length = stack_length
        self.contents_as_counter = Counter()
        self.contents_as_deque = deque(maxlen=stack_length)

    def __contains__(self, item) -> bool:
        return self.contents_as_counter[item] > 0

    def append(self, item):
        if len(self.contents_as_deque) == self.stack_length:
            removed = self.contents_as_deque.popleft()
            self.contents_as_counter.subtract(removed)

        self.contents_as_deque.append(item)
        self.contents_as_counter.update(item)


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        out = ""
        previous_k_chars = StackSet(k)
        for char in s:
            if char not in previous_k_chars:
                out += char
                previous_k_chars.append(char)

        return out


class StackSetTest(unittest.TestCase):
    def test_apend_to_empty(self):
        stack_set = StackSet(1)

        self.assertFalse("a" in stack_set)

        stack_set.append("a")
        self.assertTrue("a" in stack_set)

    def test_append_to_filled(self):
        stack_set = StackSet(1)
        stack_set.append("a")
        stack_set.append("b")
        self.assertFalse("a" in stack_set)
        self.assertTrue("b" in stack_set)

    def test_long_set(self):
        stack_set = StackSet(2)

        stack_set.append("a")
        stack_set.append("b")
        stack_set.append("c")
        stack_set.append("d")

        self.assertFalse("a" in stack_set)
        self.assertFalse("b" in stack_set)
        self.assertTrue("c" in stack_set)
        self.assertTrue("d" in stack_set)


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
