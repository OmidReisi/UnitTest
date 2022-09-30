import unittest
from unittest.mock import patch
from employee import Employee

# unittest has submodule called mock that is used when we want to simulate a test for an action but we don't want to do that thing, it's usually used for external dependencies.
# for example we want to test if our script connets to the database, in this case we actually don't want to connet to the database everytime the test is ran.
# connecting to a webpage or an api or doing some system commands are another examples of using mock objects.
# in this case we're requesting a webpage but we don't want our test to fail if the page is down because in that case our script might be fine but because the page is down our test will fail, so we mock the request and so our test dosen't have to actually connect to the page.

# we can use unittest.mock.patch to automatically mock an object without creating a mock-object.
# all we have to do is to pass the path to the object we want to mock in the place it is used as an argument.
# we can use patch as context manager, decorator, or inline(starting and closing manually)
# the best way to use patch is with context managers.
# patch has two optional arguments, return value that sets the mock-object returned value, and side effect that you can use to raise an exception or run a function or...


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

        self.assertEqual(self.emp_1.email, "Omid.Reisi@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Reisi@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("TEST FULLNAME...")

        self.assertEqual(self.emp_1.fullname, "Omid Reisi")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Reisi")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("TEST APPLY_RAISE...")

        self.assertEqual(self.emp_1.pay, 50000)
        self.assertEqual(self.emp_2.pay, 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):

        with patch("employee.requests.get") as mocked_get:

            # we want our mock-object to simulate when to request is successful so we set it's return value.ok(as in response.ok) to True, and the returned text to Success
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            

            schedule = self.emp_1.monthly_schedule("May")

            # with this we can see if our mock-object is called with the right arguments(correct url)
            mocked_get.assert_called_with("https://company.com/Reisi/May")
            self.assertEqual(schedule, "Success")

            # for simulating when request fails we don't need to set the returned text because in our main script it's set to "Bad Response!"
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("https://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
