import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return


def listFromNodes(l: ListNode) -> list[int]:
    if l.next is None:
        return [l.val]

    return [l.val] + listFromNodes(l.next)


def nodesFromList(l: list[int]) -> ListNode:
    if len(l) == 0:
        return None

    return ListNode(l[0], nodesFromList(l[1:]))


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        def _addTwoNumbers(
            l1: ListNode | None, l2: ListNode | None, carry
        ) -> ListNode | None:
            if l1 is None and l2 is None:
                if carry > 0:
                    return ListNode(carry)
                else:
                    return None

            if l1 is not None:
                l1_val = l1.val
                next_l1 = l1.next
            else:
                l1_val = 0
                next_l1 = None

            if l2 is not None:
                l2_val = l2.val
                next_l2 = l2.next
            else:
                l2_val = 0
                next_l2 = None

            sum_val = l1_val + l2_val + carry
            carry = sum_val // 10
            val = sum_val % 10

            return ListNode(val, _addTwoNumbers(next_l1, next_l2, carry))

        return _addTwoNumbers(l1, l2, 0)


class HelperTests(unittest.TestCase):
    def test_list_from_nodes(self):
        self.assertEqual([0], listFromNodes(ListNode(0)))
        self.assertEqual([5], listFromNodes(ListNode(5)))
        self.assertEqual([8, 2], listFromNodes(ListNode(8, ListNode(2))))
        self.assertEqual(
            [5, 4, 7, 6],
            listFromNodes(ListNode(5, ListNode(4, ListNode(7, ListNode(6))))),
        )

    def test_nodes_from_list(self):
        self.assertEqual([5], listFromNodes(nodesFromList([5])))
        self.assertEqual([8, 2], listFromNodes(nodesFromList([8, 2])))
        self.assertEqual(
            [5, 4, 7, 6],
            listFromNodes(nodesFromList([5, 4, 7, 6])),
        )


class SolutionTests(unittest.TestCase):
    def test_samples(self):
        tests = [
            [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
            [[0], [0], [0]],
            [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]],
        ]

        s = Solution()

        for l1, l2, expect in tests:
            self.assertEqual(
                expect,
                listFromNodes(s.addTwoNumbers(nodesFromList(l1), nodesFromList(l2))),
            )


if __name__ == "__main__":
    unittest.main()
