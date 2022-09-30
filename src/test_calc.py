# the naming convention for testing is to start with "test_" following with the file you're testing.

# in order to use the unittest module we import both the standard library's unittest and the file we're testing.
import unittest
import calc


# we create a Test class and create our test methods inside of it.
# we inherit from unittest.TestCase to use the functionality of unittest in our Test Class.
# you can see the available assertions here: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug.
# all the test methods must start with "test_" followed by the the name of the function we're testing.
class TestCalc(unittest.TestCase):

    # every test method counts as 1 test no matter how many assertions it contains.
    # the trick to writting good tests is to be mindful of edge cases and making sure your tests cover all the possible mistakes
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, -5), -5)
        self.assertEqual(calc.add(0, 5), 5)

    def test_substract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        self.assertEqual(calc.subtract(0, -5), 5)
        self.assertEqual(calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(0, -5), 0)
        self.assertEqual(calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(0, -5), 0)
        self.assertEqual(calc.divide(0, 5), 0)
        # this one checks that our division is not a floor division.
        self.assertEqual(calc.divide(5, 2), 2.5)

        # in order to check for exceptions and raised errors we use the following mehtod : assertRaises(exception, callable, *args, **kwds)
        # it's better to use assertRaises with a context manager like the following.
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)


# in order to run test module we can't run them directly with python, instead we have to run the unittest module and pass our test module as an argument.(python -m unittest test_calc.py)
# but the better way to run a test module directly is to use the lines below.


# the output in the terminal shows a . for every successful test (assertion) and a OK at the end if all tests are successful.
# the output in the terminal shows a F for every failed test (assertion) and a FAILED at the end if any of the tests fail.
# if the test method don't start with "test_" then unittest doesn't recognize them as tests and doesn't run them.
if __name__ == "__main__":
    unittest.main()
