"""
To run the unittest from CMD or Pycharm terminal,
Step1. set your python workspace(or project) in PYTHONPATH environment variable
Step2. set your PYTHONPATH environment variable into Path variable
Step3. Run the command as mentioned in the reference folder's image
"""

import unittest

class Unit_Test_Demo1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('This runs : Before Every Class')

    def setUp(self):
        print('This runs : Before Every Method')

    def test_method1(self):
        print('method 1')

    def test_method2(self):
        print('method 2')

    def test_method3(self):
        print('method 3')

    def tearDown(self):
        print('This runs : After Method')

    @classmethod
    def tearDownClass(self):
        print('This runs : After Class')


if __name__ == '__main__':
    unittest.main(verbosity=2)
