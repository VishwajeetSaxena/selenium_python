import pytest

from pytest_advance3.SampleLibraryClass import SampleLibraryClass


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def localSetup(self):
        self.obj = SampleLibraryClass(11)

    def test_methodB(self, oneTimeSetUp):
        print('#*#*#*#*#*#* Running Demo1 Method B #*#*#*#*#*#*')
        print(self.driver)
        print(self.obj.sumNumber(1, 10))
        assert False

    def test_methodA(self):
        print('#*#*#*#*#*#* Running Demo1 Method A #*#*#*#*#*#*')
        print(self.obj.sumNumber(1, 10))
        assert True

    def test_methodC(self):
        print('#*#*#*#*#*#* Running Demo1 Method C #*#*#*#*#*#*')
        assert 20 == 10


    def test_methodD(self):
        print('#*#*#*#*#*#* Running Demo1 Method D #*#*#*#*#*#*')

    def test_methodE(self):
        print('#*#*#*#*#*#* Running Demo1 Method E #*#*#*#*#*#*')

    def test_methodF(self):
        print('#*#*#*#*#*#* Running Demo1 Method F #*#*#*#*#*#*')
