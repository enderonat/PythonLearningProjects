import unittest
from employment import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Ender', 'Güraslan', 3000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 8000)

    def test_give_custom_raise(self):
        self.employee.give_raise(9000)
        self.assertEqual(self.employee.salary, 12000)
