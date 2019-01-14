import unittest


def divide_two_values(a, b):
    try:
        value = a / b
        print("The value is " + value)
    except ZeroDivisionError:
        print("Value could not be printed due to an error")


class TestCases(unittest.TestCase):

    def testDividingByZeroErrorIsHandled(self):
        divide_two_values(1, 0)

if __name__ == "__init__":
    unittest.main()
