import pytest

@pytest.fixture()
def setUp():
    print('RUNNING THIS BEFORE EVERY METHOD')
    yield
    print('RUNNING THIS AFTER EVERY METHOD')

@pytest.fixture(scope="class")
def oneTimeSetUp(browser,osType):

    print('Browser Type is: ', browser)
    print('OS Type is: ', osType)
    if browser == 'firefox':
        print('Firefox browser settings will be here')
    else:
        print('Chrome browser settings will be here')


    print('RUNNING THIS BEFORE : Based on the scope')
    yield
    print('RUNNING THIS AFTER : Based on the scope')


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help="Type of operating system")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')

