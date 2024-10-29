import unittest
from math_quiz import random_integer, random_operator, calculation


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # TODO
        # Test if the operator is either + or - or *
        operators = ["+", "-", "*"]
        for _ in range(1000):  # Test a large number of random operators
            op = random_operator()
            self.assertIn(op, operators)

    def test_calculation(self):
            test_cases = [
                 # test plus
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
                (-1, -4, '+', '-1 + -4', -5),
                (-10, 4, '+', '-10 + 4', -6),
                (10, -4, '+', '10 + -4', 6),
                # Test minus
                (3, 4, '-', '3 - 4', -1),
                (10, -10, '-', '10 - -10', 20),
                (-5, 10, '-', '-5 - 10', -15),
                (-4, -7, '-', '-4 - -7', -11),
                # Test multiply
                (2, 0, '*', '2 * 0', 0),
                (0, -3, '*', '0 * -3', 0),
                (-3, -4, '*', '-3 * -4', 12),
                (-13, 4, '*', '-13 * 4', -52),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                # Test if the calculation is correct
                prob, ans = calculation(num1, num2, operator)
                self.assertEqual(prob, expected_problem)
                self.assertEqual(ans, expected_answer)

if __name__ == "__main__":
    unittest.main()
