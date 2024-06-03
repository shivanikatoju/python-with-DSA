import pytest

@pytest.fixture
def someFun():
    print('\nSetup: Initialization here')
    yield
    print('\nTeardown: cleaning up here')

class TestClassOne:
    def testOne(self, someFun):
        print(f'\n in testOne()')
        assert True

    def testTwo(self, someFun):
        print(f'\n in testTwo()')
        assert True