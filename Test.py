import unittest
from Tasks import task1, task2, task3, task6, task7

# helper function to calculate profit
def total_profit(A, transactions):
    profit = 0
    for i, j1, j2 in transactions:
        profit += A[i][j2] - A[i][j1]
    return profit

class TestTask1(unittest.TestCase):

    def test_basic(self):
        A = [
            [7, 1, 5, 3, 6],
            [2, 4, 3, 7, 9],
            [5, 8, 9, 1, 2],
            [9, 3, 14, 8, 7]
        ]
        self.assertEqual(task1(A), (3, 1, 2, 11))

    def test_no_profit(self):
        A = [[5, 4, 3, 2, 1]]
        self.assertEqual(task1(A), (0, 0, 0, 0))

    def test_single_stock(self):
        A = [[1, 2, 3, 4, 5]]
        self.assertEqual(task1(A)[3], 4)

    def test_single_day(self):
        A = [[5], [3], [8]]
        self.assertEqual(task1(A), (0, 0, 0, 0))

    def test_all_same_prices(self):
        A = [[3, 3, 3, 3]]
        self.assertEqual(task1(A), (0, 0, 0, 0))

    def test_zero_prices(self):
        A = [[0, 0, 5, 0]]
        self.assertEqual(task1(A)[3], 5)

    def test_profit_on_last_day(self):
        A = [[1, 2, 3, 4, 10]]
        self.assertEqual(task1(A)[3], 9)


class TestTask2(unittest.TestCase):

    def test_basic(self):
        A = [
            [7, 1, 5, 3, 6],
            [2, 4, 3, 7, 9],
            [5, 8, 9, 1, 2],
            [9, 3, 14, 8, 7]
        ]
        self.assertEqual(task2(A), (3, 1, 2, 11))

    def test_no_profit(self):
        A = [[5, 4, 3, 2, 1]]
        self.assertEqual(task2(A), (0, 0, 0, 0))

    def test_single_stock(self):
        A = [[1, 2, 3, 4, 5]]
        self.assertEqual(task2(A)[3], 4)

    def test_single_day(self):
        A = [[5], [3], [8]]
        self.assertEqual(task2(A), (0, 0, 0, 0))

    def test_all_same_prices(self):
        A = [[3, 3, 3, 3]]
        self.assertEqual(task2(A), (0, 0, 0, 0))

    def test_zero_prices(self):
        A = [[0, 0, 5, 0]]
        self.assertEqual(task2(A)[3], 5)

    def test_profit_on_last_day(self):
        A = [[1, 2, 3, 4, 10]]
        self.assertEqual(task2(A)[3], 9)

# remaining tests go here

if __name__ == "__main__":
    # show passing tests
    unittest.main(verbosity=2)