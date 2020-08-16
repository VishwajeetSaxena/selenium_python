import pytest

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class TestClassDemo():


    def test_methodB(self):
        print('#*#*#*#*#*#* Running Demo1 Method B #*#*#*#*#*#*')

    def test_methodA(self):
        print('#*#*#*#*#*#* Running Demo1 Method A #*#*#*#*#*#*')

    def test_methodC(self):
        print('#*#*#*#*#*#* Running Demo1 Method C #*#*#*#*#*#*')

    def test_methodD(self):
        print('#*#*#*#*#*#* Running Demo1 Method D #*#*#*#*#*#*')

    def test_methodE(self):
        print('#*#*#*#*#*#* Running Demo1 Method E #*#*#*#*#*#*')

    def test_methodF(self):
        print('#*#*#*#*#*#* Running Demo1 Method F #*#*#*#*#*#*')
