from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        result = solution([[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]])

        self.assertEqual(result, [2, 4, 3, 1, 5, 6, 9, 7, 9, 0])
