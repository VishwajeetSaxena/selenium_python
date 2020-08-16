import unittest

class Unit_Test_Demo(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('This runs : Before Every Class')

    def setUp(self):
        print('This runs : Before Every Method')

    def test_method1(self):
        print('method 1')
        a = True
        self.assertTrue(a, 'FAILURE MESSAGE : This Message Will Be Shown If Condition Is Not As Expected')
        b = True
        self.assertFalse(b, 'FAILURE MESSAGE : This Message Will Be Shown If Condition Is Not As Expected')

    def test_method2(self):
        print('method 2')
        a = 1
        b = 2

        self.assertEqual(a, b, 'FAILURE MESSAGE : Actual Results Is Not As Expected')

    def test_method3(self):
        print('method 3')


    def tearDown(self):
        print('This runs : After Method')

    @classmethod
    def tearDownClass(self):
        print('This runs : After Class')


if __name__ == '__main__':
    unittest.main(verbosity=2)

