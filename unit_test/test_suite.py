"""
To run the test suites from CMD or Pycharm terminal,
Step1. set your python workspace(or project) in PYTHONPATH environment variable
Step2. set your PYTHONPATH environment variable into Path variable
Step3. Run the command as mentioned in the reference folder's image
"""

import unittest

from unit_test.unit_tc_demo1 import Unit_Test_Demo1
from unit_test.unit_tc_demo2 import Unit_Test_Demo2

# Get the collection of test cases from different classes
testcase_from_class1 = unittest.TestLoader().loadTestsFromTestCase(Unit_Test_Demo1)
testcase_from_class2 = unittest.TestLoader().loadTestsFromTestCase(Unit_Test_Demo2)

# Create Test Suites
smoke_test = unittest.TestSuite([testcase_from_class1])

regression_test = unittest.TestSuite([testcase_from_class1, testcase_from_class2])

# Create Test Runner
# unittest.TextTestRunner(verbosity=2).run(smoke_test)
unittest.TextTestRunner(verbosity=2).run(regression_test)
