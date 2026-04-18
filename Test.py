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

class TestTask3(unittest.TestCase):

    def test_basic(self):
        A = [
            [7, 1, 5, 3, 6],
            [2, 4, 3, 7, 9],
            [5, 8, 9, 1, 2],
            [9, 3, 14, 8, 7]
        ]
        self.assertEqual(task3(A), (3, 1, 2, 11))

    def test_no_profit(self):
        A = [[5, 4, 3, 2, 1]]
        self.assertEqual(task3(A), (0, 0, 0, 0))

    def test_single_stock(self):
        A = [[1, 2, 3, 4, 5]]
        self.assertEqual(task3(A)[3], 4)

    def test_agrees_with_task1(self):
        # task 3 should always produce the same profit as task 1
        A = [
            [12, 1, 5, 3, 16],
            [4, 4, 13, 4, 9],
            [6, 8, 6, 1, 2],
            [14, 3, 4, 8, 10]
        ]
        self.assertEqual(task1(A)[3], task3(A)[3])


class TestTask6(unittest.TestCase):

    def setUp(self):
        self.A = [
            [2, 9, 8, 4, 5, 0, 7],
            [6, 7, 3, 9, 1, 0, 8],
            [1, 7, 9, 6, 4, 9, 11],
            [7, 8, 3, 1, 8, 5, 2],
            [1, 8, 4, 0, 9, 2, 1]
        ]
        self.c = 2

    def test_basic_profit(self):
        result = task6(self.A, self.c)
        self.assertEqual(total_profit(self.A, result), 16)

    def test_no_profit(self):
        A = [[5, 4, 3, 2, 1, 0]]
        self.assertEqual(task6(A, 1), [])

    def test_cooldown_respected(self):
        result = task6(self.A, self.c)
        for idx in range(len(result) - 1):
            _, _, sell_day = result[idx]
            _, buy_day, _ = result[idx + 1]
            self.assertGreaterEqual(buy_day, sell_day + self.c + 1)


class TestTask7(unittest.TestCase):

    def setUp(self):
        self.A = [
            [2, 9, 8, 4, 5, 0, 7],
            [6, 7, 3, 9, 1, 0, 8],
            [1, 7, 9, 6, 4, 9, 11],
            [7, 8, 3, 1, 8, 5, 2],
            [1, 8, 4, 0, 9, 2, 1]
        ]
        self.c = 2

    def test_basic_profit(self):
        result = task7(self.A, self.c)
        self.assertEqual(total_profit(self.A, result), 16)

    def test_no_profit(self):
        A = [[5, 4, 3, 2, 1, 0]]
        self.assertEqual(task7(A, 1), [])

    def test_cooldown_respected(self):
        result = task7(self.A, self.c)
        for idx in range(len(result) - 1):
            _, _, sell_day = result[idx]
            _, buy_day, _ = result[idx + 1]
            self.assertGreaterEqual(buy_day, sell_day + self.c + 1)

    def test_agrees_with_task6(self):
        # task 7 should always produce the same total profit as task 6
        self.assertEqual(
            total_profit(self.A, task6(self.A, self.c)),
            total_profit(self.A, task7(self.A, self.c))
        )

if __name__ == "__main__":
    # show passing tests
    unittest.main(verbosity=2)
