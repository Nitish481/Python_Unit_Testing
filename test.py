import unittest
from emp import employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = employee('Nitish','Mandal',25000)
        self.emp2 = employee('Abhijit', 'Das', 50000)

    def test_email(self):
        self.assertEqual(self.emp1.email, 'Nitish.Mandal@email.com')
        self.assertEqual(self.emp2.email, 'Abhijit.Das@email.com')

        self.emp1.first = 'Nikhil'
        self.emp2.first = 'Abhay'

        self.assertEqual(self.emp1.email, 'Nikhil.Mandal@email.com')
        self.assertEqual(self.emp2.email, 'Abhay.Das@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Nitish Mandal')
        self.assertEqual(self.emp2.fullname, 'Abhijit Das')

        self.emp1.first = 'Nikhil'
        self.emp2.first = 'Abhay'

        self.assertEqual(self.emp1.fullname, 'Nikhil Mandal')
        self.assertEqual(self.emp2.fullname, 'Abhay Das')

    

if __name__ == '__main__':
    unittest.main()
