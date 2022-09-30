import unittest
from employee import Employee


# as we can see we're creating two new employees at the start of each test and repeating ourselves over and over again
# in order to avoid repetition we can use the following methods:
# setUp(self) : this method runs at the start of each test.
# tearDown(self): this method runt at the end of each test.
# the following methods are two class methods that only run once:
# setUpClass(cls): runs once before the start of testing.
# tearDownClass(cls): runs once after all tests are done.
class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("STRAT TESTING...\n")

    @classmethod
    def tearDownClass(cls):
        print("ALL TESTS ARE DONE...")

    def setUp(self):
        self.emp_1 = Employee("Omid", "Reisi", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    def tearDown(self):
        print("TEST FINISHED...\n")

    def test_email(self):
        print("TEST EMAIL...")
        # emp_1 = Employee("Omid", "Reisi", 50000)
        # emp_2 = Employee("Sue", "Smith", 60000)

        self.assertEqual(self.emp_1.email, "Omid.Reisi@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Reisi@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("TEST FULLNAME...")
        # emp_1 = Employee("Omid", "Reisi", 50000)
        # emp_2 = Employee("Sue", "Smith", 60000)

        self.assertEqual(self.emp_1.fullname, "Omid Reisi")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Reisi")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("TEST APPLY_RAISE...")
        # emp_1 = Employee("Omid", "Reisi", 50000)
        # emp_2 = Employee("Sue", "Smith", 60000)

        self.assertEqual(self.emp_1.pay, 50000)
        self.assertEqual(self.emp_2.pay, 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


# note that tests might not be ran in order they're created so it's important to keep the tests isolated.
if __name__ == "__main__":
    unittest.main()
