import pytest

@pytest.fixture()
def setUp1():
    print('Setup 1')

@pytest.fixture()
def setUp2():
    print('Setup 2')

def test_methodA(setUp1):
    print('#*#*#*#*#*#* Running Method A ')

def test_methodB(setUp1):
    print('#*#*#*#*#*#* Running Method B')
