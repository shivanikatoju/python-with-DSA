import pytest

@pytest.fixture
def someFunction():
    print('\nSetup: Initialization process')
    yield
    print('\nTeardown: cleaning up resources')

def testTrue(someFunction):
    print('#1. My test functions: performing testing')
    assert True

def testIsTrue(someFunction):
    print('#2. My test functions: performing testing')
    assert True