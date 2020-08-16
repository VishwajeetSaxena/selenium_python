import pytest

@pytest.fixture()
def setUp():
    print('RUNNING THIS BEFORE EVERY METHOD')
    yield
    print('RUNNING THIS AFTER EVERY METHOD')

@pytest.fixture(scope="module")
def oneTimeSetUp():
    print('RUNNING THIS BEFORE : Based on the scope')
    yield
    print('RUNNING THIS AFTER : Based on the scope')
