"""
file name should start with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose

@pytest.yield_fixture() // No meed of yield_fixture instead of fixture from pytest 2.10 version
"""

import pytest

# @pytest.yield_fixture() // No meed of yield_fixture instead of fixture from pytest 2.10 version
@pytest.fixture()
def setUp():
    print('RUNNING THIS BEFORE EVERY METHOD')
    yield
    print('RUNNING THIS AFTER EVERY METHOD')

def test_methodA(setUp):
    print('#*#*#*#*#*#* Running Method A #*#*#*#*#*#*')

def test_methodB(setUp):
    print('#*#*#*#*#*#* Running Method B #*#*#*#*#*#*')
